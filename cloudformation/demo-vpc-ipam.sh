#!/bin/bash

start_time=$(date +%s)

# First command
curl -O https://raw.githubusercontent.com/alivk/aws-demo/main/cloudformation/demo-vpc-ipam.yml

# Second command
aws cloudformation create-stack \
  --stack-name demo-vpc-ipam \
  --template-body file://demo-vpc-ipam.yml \
  --capabilities CAPABILITY_IAM \
  --parameters \
  ParameterKey=TagEnvironment,ParameterValue=Production \
  ParameterKey=OrganizationId,ParameterValue=o-nlcyaid4qo \
  ParameterKey=ManagementAccountId,ParameterValue=942368217596

# Third command
aws cloudformation wait stack-create-complete --stack-name demo-vpc-ipam

# Fourth command
echo -e "The Cloudformation Stack is Ready!!\n\n"

end_time=$(date +%s)
execution_time=$((end_time - start_time))
echo "Total execution time: ${execution_time} seconds"
