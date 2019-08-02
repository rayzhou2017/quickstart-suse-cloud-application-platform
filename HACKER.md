# quickstart-suse-cloud-application-platform
## Deploying from source

Deploying from source:

1) git clone https://github.com/kbaegis/quickstart-suse-cloud-application-platform.git
2) git -C $(pwd)/quickstart-suse-cloud-application-platform/ submodule update --init --recursive
3) Make changes to code
4) aws s3 mb bucket
5) aws s3 sync $(pwd)/quickstart-suse-cloud-application-platform/ s3://bucket/version/ --exclude '.git/*' --exclude '*/.git/*'
6) aws cloudformation create-stack --stack-name stackname --template-url s3://bucket/version/templates/suse-cap-master.template.yaml
7) cf login --skip-ssl-validation -a <CfApiEndpoint Output>
  - user: admin
  - password: <AWS Secrets Manager AdminPassword>

##Testing
cf create-org SUSE
cf create-space DEMO
cf target -s DEMO
git clone https://github.com/troytop/dizzylizard
cf push

##Links
[deployment guide](https://fwd.aws/eb5pW).
[AWS Quick Start Contributor's Kit](https://aws-quickstart.github.io/). 
