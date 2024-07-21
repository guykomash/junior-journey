from dotenv import load_dotenv
load_dotenv()
import logging
import boto3
import uuid
import os
from botocore.exceptions import ClientError

# def singelton(class_):
#     instances = {}
#     def get_instance(*args, **kwargs):
#         if class_ not in instances:
#             instances[class_] = class_(*args, **kwargs)
#         return instances[class_]
#     return get_instance

# @singelton
# class S3_CLIENT():
#     def __init__(self):
#         self.bucket_name = os.getenv(os.getenv('S3_BUCKET_NAME'))
#         self.s3_client = boto3.client('s3',
#                 aws_access_key_id=os.getenv('S3_ACCESS_KEY'),
#                 aws_secret_access_key=os.getenv('S3_SECRET_ACCESS_KEY'),
#                 region_name=os.getenv("S3_REGION"))

AWS_ACCESS_KEY = os.getenv('S3_ACCESS_KEY')
AWS_SECRET_KEY = os.getenv('S3_SECRET_ACCESS_KEY')
AWS_REGION = os.getenv('S3_REGION')
BUCKET_NAME = os.getenv("S3_BUCKET_NAME")

ALLOWED_FILE_TYPES = ['pdf']

s3 = boto3.client('s3',
        aws_access_key_id=AWS_ACCESS_KEY, 
        aws_secret_access_key=AWS_SECRET_KEY, 
        region_name=AWS_REGION
    )

def create_presigned_url(user_id,filename):
    object_name = f"{user_id}-{filename}"
    print(f"object_name = {object_name}")

    s3_client = boto3.client('s3')
    try:
        presigned_url = s3_client.generate_presigned_url(
            'put_object',
            Params={'Bucket': BUCKET_NAME, 'Key': object_name},
            ExpiresIn=3600
        )
    except ClientError as e:
        print('s3Client error')
        print(e)
        return None

    # The response contains the presigned URL
    print(presigned_url)
    return presigned_url


    

