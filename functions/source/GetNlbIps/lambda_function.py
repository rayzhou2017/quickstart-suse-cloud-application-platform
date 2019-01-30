import json
import logging
import threading
from botocore.vendored import requests
import boto3
from time import sleep
import socket


SUCCESS = "SUCCESS"
FAILED = "FAILED"


elbv2_client = boto3.client('elbv2')


def send(event, context, response_status, response_data, physical_resource_id, reason=None):
    response_url = event['ResponseURL']
    logging.debug("CFN response URL: " + response_url)
    response_body = dict()
    response_body['Status'] = response_status
    msg = 'See details in CloudWatch Log Stream: ' + context.log_stream_name
    if not reason:
        response_body['Reason'] = msg
    else:
        response_body['Reason'] = str(reason)
    if physical_resource_id:
        response_body['PhysicalResourceId'] = physical_resource_id
    elif 'PhysicalResourceId' in event:
        response_body['PhysicalResourceId'] = event['PhysicalResourceId']
    else:
        response_body['PhysicalResourceId'] = context.log_stream_name
    response_body['StackId'] = event['StackId']
    response_body['RequestId'] = event['RequestId']
    response_body['LogicalResourceId'] = event['LogicalResourceId']
    if response_data and response_data != {} and response_data != [] and isinstance(response_data, dict):
        response_body['Data'] = response_data
    json_response_body = json.dumps(response_body)
    logging.debug("Response body:\n" + json_response_body)
    headers = {
        'content-type': '',
        'content-length': str(len(json_response_body))
    }
    print("Returning response: %s" % json_response_body)
    try:
        response = requests.put(response_url, data=json_response_body, headers=headers)
        logging.info("CloudFormation returned status code: " + response.reason)
    except Exception as e:
        logging.error("send(..) failed executing requests.put(..): " + str(e))
        raise


def timeout(event, context):
    logging.error('Execution is about to time out, sending failure response to CloudFormation')
    send(event, context, FAILED, {}, None)


def lambda_handler(event, context):
    # make sure we send a failure to CloudFormation if the function is going to timeout
    timer = threading.Timer((context.get_remaining_time_in_millis() / 1000.00) - 0.5, timeout, args=[event, context])
    timer.start()
    print('Received event: %s' % json.dumps(event))
    status = SUCCESS
    response_data = {}
    physical_resource_id = None
    error_message = None
    try:
        if event['RequestType'] in ['Create', 'Update']:
            while True:
                response = elbv2_client.describe_load_balancers(LoadBalancerArns=[event['ResourceProperties']['NlbArn']])
                if response['LoadBalancers'][0]['State']['Code'] == 'active':
                    ips = socket.gethostbyname_ex(response['LoadBalancers'][0]['DNSName'])[2]
                    response_data['Ip1'] = ips[0]
                    response_data['Ip2'] = ips[1]
                    response_data['Ip3'] = ips[2]
                    break
                sleep(5)
    except Exception as e:
        logging.error('Exception: %s' % e, exc_info=True)
        status = FAILED
        error_message = str(e)
    finally:
        timer.cancel()
        send(event, context, status, response_data, physical_resource_id, reason=error_message)
