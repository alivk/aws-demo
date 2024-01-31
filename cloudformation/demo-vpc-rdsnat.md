**Create VPC and RDS NAT Cloudformation Stack for monilith application**

The following Cloudformation template will create by following the steps in this section:
The CloudFormation template defines a virtual private cloud. 
The Amazon Virtual Private Cloud (Amazon VPC) is called Lab VPC, 
and it contains four network subnets: 
two are public (which means compute instances assigned to these subnets can be accessed directly from the internet)
and two are private (compute instances assigned to these subnets use private IP addresses and cannot be directly accessed from the internet). 

The template also specifies a Network Address Translation (NAT for short) instance
that performs a mapping between the internal IP addresses of hosts that route through it
and an external IP address so that even though the instances have private addresses,
they can still retrieve data from the internet. 
Lastly is the RDS MySQL database and NAT instance.

**Cloudformation template**

[demo-vpc-rdsnat.yml](demo-vpc-rdsnat.yml)

**Expected Cloudshell script**
Go to Cloudshell environment (Singapore) and execute following command
```
var='demo-vpc-rdsnat'
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
