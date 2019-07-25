# quickstart-suse-cloud-application-platform
## Updates

Steps for upgrading the CAP version:

- helm repo add suse https://kubernetes-charts.suse.com
- helm repo update
- helm search -l suse/cf
- helm search -l suse/uaa
- helm fetch --version `version` -d $(pwd)/charts suse/cf
- helm fetch --version `version` -d $(pwd)/charts suse/uaa

##Links
![Quick Start architecture for SUSE Cloud Application Platform on AWS](https://d0.awsstatic.com/partner-network/QuickStart/datasheets/suse-cap-architecture-on-aws.png)
[deployment guide](https://fwd.aws/eb5pW).
[AWS Quick Start Contributor's Kit](https://aws-quickstart.github.io/). 
