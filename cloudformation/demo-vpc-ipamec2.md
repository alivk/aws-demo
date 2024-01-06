**Create Amazon VPC IPAM Manager Support EC2 Cloudformation Stack**

The following Cloudformation template will create by following the steps in this section:

- VPC
- Some Subnet part of IPAM Prod pool
- 4 x EC2 instances

Please take note this stack have no dependancy with IPAM yet as still using "manual" way of creating VPC.

**Cloudformation template**

[demo-vpc-ipamec2.yml](demo-vpc-ipamec2.yml)

**Expected Cloudshell script**
Go to Cloudshell environment (Singapore) and execute following command

```
# Download the script from your GitHub repository
curl -O https://raw.githubusercontent.com/alivk/aws-demo/main/cloudformation/demo-vpc-ipamec2.sh
# Make the script executable:
chmod +x demo-vpc-ipamec2.sh
# Run the script:
./demo-vpc-ipamec2.sh
```

**Expected Ouput**
```
STEP01 - Starting the stack demo-vpc-ipamec2 creation (average time around 93 seconds) ...
STEP02 - Downloading the CloudFormation template...
STEP03 - Creating the CloudFormation stack...
STEP04 - Waiting for CloudFormation stack creation to complete... running... 
STEP05 - The CloudFormation Stack demo-vpc-ipamec2 is Ready!!!
STEP06 - Stack demo-vpc-ipam completed, Total execution time: 93 seconds
```
