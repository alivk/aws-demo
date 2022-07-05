# This is Alick modified copy with pause function for class demo purpose.

"""
Purpose
Demonstrates how to use Amazon S3 select csv
"""

import boto3


s3 = boto3.client('s3')

s3_bucket_name = input("Please enter your bucket name: [default:alick-private-demo] \n")
if len(s3_bucket_name) == 0 :
    s3_bucket_name = "alick-private-demo"

resp = s3.select_object_content(
    Bucket=s3_bucket_name,
    Key='python-s3-select-csv.csv',
    ExpressionType='SQL',
    Expression="SELECT * FROM s3object s where s.\"Name\" = 'Alick'",
    InputSerialization = {'CSV': {"FileHeaderInfo": "Use"}, 'CompressionType': 'NONE'},
    OutputSerialization = {'CSV': {}},
)


for event in resp['Payload']:
    if 'Records' in event:
        records = event['Records']['Payload'].decode('utf-8')
        print("===========  S3 Select Output as shown as following ===========")
        print(records)
    elif 'Stats' in event:
        statsDetails = event['Stats']['Details']
        print("=========  S3 Select Stats Info as shown as following =========")
        print("Stats details bytesScanned: " + str(statsDetails['BytesScanned']))
        print("Stats details bytesProcessed: " + str(statsDetails['BytesProcessed']))
        print("Stats details bytesReturned: " + str(statsDetails['BytesReturned']))