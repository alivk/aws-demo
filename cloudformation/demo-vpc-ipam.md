**Create Amazon VPC IPAM Manager Cloudformation Stack**

The following Cloudformation template will create by following the steps in this section:

- IPAM operating in AWS Region 1(ap-southeast-1), AWS Region 2(us-west-2)
- Private scope
- Top-level pool
- Regional pool in different region

**Cloudformation template**

[demo-vpc-ipam.yml](demo-vpc-ipam.yml)

**Expected Cloudshell script**
Go to Cloudshell environment (Singapore) and execute following command
```
var='demo-vpc-ipam'
```
then perform the script execution

```
curl -O https://raw.githubusercontent.com/alivk/aws-demo/main/cloudformation/$var.sh
chmod +x $var.sh
./$var.sh
```

**Expected Ouput**
```
STEP01 - Starting the stack creation (average time around 93 seconds) ...
STEP02 - Downloading the CloudFormation template...
STEP03 - Creating the CloudFormation stack...
STEP04 - Waiting for CloudFormation stack creation to complete... running... 
STEP05 - The CloudFormation Stack is Ready!!!
STEP06 - Stack completed, Total execution time: 93 seconds
```
```
