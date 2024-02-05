import json
import boto3
import requests  # Import requests
from botocore.exceptions import ClientError

def get_current_ip_address():
    try:
        response = requests.get('https://checkip.amazonaws.com/')
        ip_address = response.text.strip()
        print(f"Current public IP address is {ip_address}/32 (https://checkip.amazonaws.com/)")
        return ip_address + "/32"
    except requests.RequestException as e:
        print("Failed to obtain current IP address:", e)

def get_current_policy(s3, bucket_name):
    try:
        result = s3.get_bucket_policy(Bucket=bucket_name)
        policy = json.loads(result['Policy'])
        print("Current policy:", json.dumps(policy, indent=2))
        return policy
    except ClientError as e:
        if e.response['Error']['Code'] == 'NoSuchBucketPolicy':
            print("No existing policy found.")
        else:
            print("An unexpected error occurred:", e)

def update_bucket_policy(s3, bucket_name, ip_address):
    policy = {
        "Version": "2012-10-17",
        "Statement": [
            {
                "Sid": "AllowPolicyManagementForAnyIP",
                "Effect": "Allow",
                "Principal": "*",
                "Action": [
                    "s3:DeleteBucketPolicy",
                    "s3:PutBucketPolicy"
                ],
                "Resource": f"arn:aws:s3:::{bucket_name}"
            },
            {
                "Sid": "DenyAllExceptPolicyManagementForNonSpecifiedIP",
                "Effect": "Deny",
                "Principal": "*",
                "Action": "s3:*",
                "Resource": [
                    f"arn:aws:s3:::{bucket_name}",
                    f"arn:aws:s3:::{bucket_name}/*"
                ],
                "Condition": {
                    "NotIpAddress": {"aws:SourceIp": ip_address}
                }
            }
        ]
    }
    try:
        s3.put_bucket_policy(Bucket=bucket_name, Policy=json.dumps(policy))
        print("Bucket policy updated to allow policy management for any IP and restrict other access.")
    except ClientError as e:
        print(f"Failed to update bucket policy: {e}")


def delete_bucket_policy(s3, bucket_name):
    try:
        s3.delete_bucket_policy(Bucket=bucket_name)
        print("Bucket policy deleted successfully.")
    except ClientError as e:
        print("Failed to delete bucket policy:", e)

def main():
    current_ip = get_current_ip_address()
    s3 = boto3.client('s3')
    choice = input("Choose an option:\n1. Create or Modify bucket policy\n2. Delete bucket policy\nOption: ")
    
    if choice == '1':
        bucket_name = input("Enter the bucket name for IP restriction: ")
        get_current_policy(s3, bucket_name)
        ip_address = input("Enter the current IP address block to add (e.g., '1.2.3.4/32'): ")
        print("New IP restriction to be added:", ip_address)
        confirm = input("Type 'yes' to apply the new bucket policy: ")
        if confirm.lower() == 'yes':
            update_bucket_policy(s3, bucket_name, ip_address)
        else:
            print("Operation cancelled.")
    elif choice == '2':
        bucket_name = input("Enter the bucket name to delete its policy: ")
        confirm = input("Are you sure you want to delete the bucket policy? Type 'yes' to confirm: ")
        if confirm.lower() == 'yes':
            delete_bucket_policy(s3, bucket_name)
        else:
            print("Operation cancelled.")
    else:
        print("Invalid option.")

if __name__ == "__main__":
    main()
