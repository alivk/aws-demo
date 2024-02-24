**Create site to site simulations between two VPCs and use Transit Gateway to connect**

The following Cloudformation template will create by following the steps in this section:
The CloudFormation template defines two VPC
one is Source-VPC which represent the on-premises infrastructure
another one is Target-VPC which is represent the AWS environment.
we are going to create the connectivity and perform AD join actions

**Cloudformation template**

[demo-vpn-sitetosite.yml](demo-vpn-sitetosite.yml)

**Expected Cloudshell script**
Go to Cloudshell environment (Singapore) and execute following command
```
var='demo-vpn-sitetosite'
```
then perform the script execution

```
curl -O https://raw.githubusercontent.com/alivk/aws-demo/main/cloudformation/$var.sh
chmod +x $var.sh
./$var.sh
```

**Expected Ouput**
```
STEP01 - Starting the stack creation (average time around 455 seconds) ...
STEP02 - Downloading the CloudFormation template...
STEP03 - Creating the CloudFormation stack...
STEP04 - Waiting for CloudFormation stack creation to complete... running... 
STEP05 - The CloudFormation Stack is Ready!!!
STEP06 - Stack completed, Total execution time: 93 seconds
```
