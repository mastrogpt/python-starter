#--kind python:default
#--web true
#--param MINIO_HOST $MINIO_HOST
#--param MINIO_PORT $MINIO_PORT
#--param MINIO_ACCESS_KEY $MINIO_ACCESS_KEY
#--param MINIO_SECRET_KEY $MINIO_SECRET_KEY

import boto3
from botocore.client import Config                                                                                                                                                                   

def main(args):
    buckets = []
    s3 = boto3.resource('s3',
                    endpoint_url=f"http://{args.get('MINIO_HOST')}:{args.get('MINIO_PORT')}",
                    aws_access_key_id=args.get("MINIO_ACCESS_KEY"),
                    aws_secret_access_key=args.get("MINIO_SECRET_KEY"),
                    config=Config(signature_version='s3v4'),
                    region_name='us-east-1')
                                                                                                                                                                              
    for bucket in s3.buckets.all():
        buckets.append(bucket.name)
    
    response = {"body": buckets}
    return response