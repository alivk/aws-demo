
#!/bin/bash

# Step 01: Start the timer

start_time=$(date +%s)
stack_name="demo-messaging-sqssnskinesisiot"
echo "STEP01 - Starting the stack "$stack_name" creation (average time around 93 seconds) ..."


# Step 02: Downloading the CloudFormation template

echo "STEP02 - Downloading the CloudFormation template..."
curl -O https://raw.githubusercontent.com/alivk/aws-demo/main/cloudformation/"$stack_name".yml

# Step 03: Creating the CloudFormation stack

echo "STEP03 - Creating the CloudFormation stack..."
aws cloudformation create-stack \
  --stack-name "$stack_name" \
  --template-body file://"$stack_name".yml \
  --capabilities CAPABILITY_NAMED_IAM

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
