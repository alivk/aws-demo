**Create a presigned URL**

Generates a presigned URL and uses the Requests package to get or 
put a file in an Amazon S3 bucket. For example, run the following command to get
a file from Amazon S3 at a command prompt.

First way 
```
aws s3 presign s3://alick-private-demo/python-s3-select-csv.csv --expires-in 20
```
here expires in is number of seconds

Second way

```
python presigned_url.py your-bucket-name your-object-key your-action your-duration
``` 
For example

```
python python-s3-presignedurl.py alick-private-demo python-s3-select-csv.csv get 1000
``` 


Run the script with the `-h` flag to get more help.