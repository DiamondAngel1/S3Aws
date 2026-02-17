import os
import boto3

#print("Сало - це смачно і дуже корисно!")
s3_client = boto3.client('s3')

response = s3_client.list_buckets()
for bucket in response['Buckets']:
    print(bucket)

response = s3_client.list_objects_v2(Bucket='transfer-siu-images')
objects = response.get('Contents', [])
print(objects)

#s3_client.download_file('transfer-siu-images', 'bobr.jpg', 'downloaded_bobr.jpg')
#s3_client.download_file('transfer-siu-images', 'info.txt', 'downloaded_info.txt')

s3_client.put_bucket_versioning(
    Bucket='my-girl-images', 
    VersioningConfiguration={'Status': 'Enabled'}
)