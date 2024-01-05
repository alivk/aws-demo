**Create Configure VPC IPAM Manager**

The following Cloudformation template will create by following the steps in this section:

- IPAM operating in AWS Region 1(ap-southeast-1), AWS Region 2(us-west-2)
- Private scope
- Top-level pool
- Regional pool in different region

**Cloudformation template**

[cloudformation-template](demo-vpc-ipam.yml)

**Expected Cloudshell script**
Go to Cloud9 environment (Singapore) 

and if we issue following command
we can see the cloudformation stack is successfully created

```
aws cloudformation create-stack \
--stack-name ipam-demo \
--template-body file://cf-ipam.yml \
--parameters \
ParameterKey=TagEnvironment,ParameterValue=Production \
ParameterKey=OrganizationId,ParameterValue=o-nlcyaid4qo \
ParameterKey=ManagementAccountId,ParameterValue=942368217596 \
--capabilities CAPABILITY_IAM
```

**Expected Ouput**
```
{
 "StackId": "arn:aws:cloudformation:ap-southeast-1:xxxxxxxx:stack/ipam-demo/942c9560-1be3-11ee-b931-06ef67cb97d6"
}
```
