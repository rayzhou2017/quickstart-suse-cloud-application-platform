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
[deployment guide](https://fwd.aws/eb5pW).
[AWS Quick Start Contributor's Kit](https://aws-quickstart.github.io/). 
