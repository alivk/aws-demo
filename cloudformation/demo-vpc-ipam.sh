#!/bin/bash

# Step 01: Start the timer

echo "STEP01 - Starting the script..."
start_time=$(date +%s)

# Step 02: Downloading the CloudFormation template

echo "STEP02 - Downloading the CloudFormation template..."
curl -O https://raw.githubusercontent.com/alivk/aws-demo/main/cloudformation/demo-vpc-ipam.yml

# Step 03: Creating the CloudFormation stack

echo "STEP03 - Creating the CloudFormation stack..."
aws cloudformation create-stack \
  --stack-name demo-vpc-ipam \
  --template-body file://demo-vpc-ipam.yml \
  --capabilities CAPABILITY_IAM \
  --parameters \
  ParameterKey=TagEnvironment,ParameterValue=Production \
  ParameterKey=OrganizationId,ParameterValue=o-nlcyaid4qo \
  ParameterKey=ManagementAccountId,ParameterValue=942368217596

# Step 04: Waiting for CloudFormation stack creation to complete

echo -n "STEP04 - Waiting for CloudFormation stack creation to complete... "
while true; do
  echo -n "STEP05 - Script is running in the background... "
  aws cloudformation wait stack-create-complete --stack-name demo-vpc-ipam &> /dev/null
  if [ $? -eq 0 ]; then
    echo "STEP06 - The CloudFormation Stack is Ready!!\n\n!"
    break
  else
    echo -n "."
    sleep 5
  fi
done

end_time=$(date +%s)
execution_time=$((end_time - start_time))
echo "STEP06 - Script completed, Total execution time: ${execution_time} seconds"
