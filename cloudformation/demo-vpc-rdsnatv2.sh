#!/bin/bash

# Step 01: Start the timer

start_time=$(date +%s)
stack_name="demo-vpc-rdsnatv2"
echo "STEP01 - Starting the stack "$stack_name" creation (average time around 93 seconds) ..."


# Step 02: Downloading the CloudFormation template

echo "STEP02 - Downloading the CloudFormation template..."
curl -O https://raw.githubusercontent.com/alivk/aws-demo/main/cloudformation/"$stack_name".yml

# Step 03: Creating the CloudFormation stack

echo "STEP03 - Creating the CloudFormation stack..."
aws cloudformation create-stack \
  --stack-name "$stack_name" \
  --template-body file://"$stack_name".yml \
  --capabilities CAPABILITY_IAM \
  --parameters \
    ParameterKey=KeyName,ParameterValue=dev \
    ParameterKey=RoleName,ParameterValue=ROLE-SSMAdminAccess \
    ParameterKey=LabVPCCIDR,ParameterValue=10.0.0.0/16 \
    ParameterKey=PublicSubnet1Param,ParameterValue=10.0.10.0/24 \
    ParameterKey=PublicSubnet2Param,ParameterValue=10.0.15.0/24 \
    ParameterKey=PrivateSubnet1Param,ParameterValue=10.0.50.0/24 \
    ParameterKey=PrivateSubnet2Param,ParameterValue=10.0.55.0/24 \
    ParameterKey=DBPassword,ParameterValue=labpassword \

# Step 04: Waiting for CloudFormation stack creation to complete

echo -n "STEP04 - Waiting for CloudFormation stack creation to complete..."

while true; do
  echo -n "running"
  aws cloudformation wait stack-create-complete --stack-name "$stack_name" &> /dev/null
  if [ $? -eq 0 ]; then
    echo "STEP05 - The CloudFormation Stack "$stack_name" is Ready!!"
    break
  else
    echo -n "."
    sleep 2
  fi
done

end_time=$(date +%s)
execution_time=$((end_time - start_time))
echo "STEP06 - Stack "$stack_name" completed, Total execution time: ${execution_time} seconds"
