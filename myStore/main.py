import os
import boto3

#print("Сало - це смачно і дуже корисно!")
s3_client = boto3.client('s3')

response = s3_client.list_buckets()
for bucket in response['Buckets']:
    print(bucket)