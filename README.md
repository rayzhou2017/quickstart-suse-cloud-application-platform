# quickstart-suse-cloud-application-platform
## SUSE Cloud Application Platform on the AWS Cloud

This Quick Start deploys SUSE Cloud Application Platform, which is a fully containerized implementation of Cloud Foundry, on the Amazon Web Services (AWS) Cloud.

SUSE Cloud Application Platform provides a modern application delivery platform for streamlining lifecycle management of traditional and cloud-native applications. It is deployed as containers in a Kubernetes cluster and provides one-step, containerized application development, a web UI (Stratos) for managing deployments, automation for application lifecycle management, and configurable service brokers through the Open Service Broker API.

SUSE Cloud Application Platform supports multiple languages and frameworks through open-source buildpacks for Java, Go, .NET, Node.js, and other environments. This deployment uses Amazon Elastic Container Service for Kubernetes (Amazon EKS) as a foundation, and provides integration with AWS Service Broker.

The Quick Start offers two deployment options:

- Deploying SUSE Cloud Application Platform into a new virtual private cloud (VPC) on AWS
- Deploying SUSE Cloud Application Platform into an existing VPC on AWS

Each deployment takes about 45 minutes.

You can also use the AWS CloudFormation templates as a starting point for your own implementation.

![Quick Start architecture for SUSE Cloud Application Platform on AWS](https://d1.awsstatic.com/partner-network/QuickStart/datasheets/suse-cap-architecture-on-aws.png)

For architectural details, best practices, step-by-step instructions, and customization options, see the 
[deployment guide](https://fwd.aws/eb5pW).

To post feedback, submit feature ideas, or report bugs, use the **Issues** section of this GitHub repo.
If you'd like to submit code for this Quick Start, please review the [AWS Quick Start Contributor's Kit](https://aws-quickstart.github.io/). 
