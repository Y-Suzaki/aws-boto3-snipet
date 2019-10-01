import boto3
import os


os.environ['AWS_DEFAULT_REGION'] = 'us-west-2'
client = boto3.client('s3')


def create(uri):
    client.create_bucket(
        Bucket=uri,
        CreateBucketConfiguration={
            'LocationConstraint': os.environ['AWS_DEFAULT_REGION']
        }
    )

    client.put_bucket_encryption(
        Bucket=uri,
        ServerSideEncryptionConfiguration={
            'Rules': [{'ApplyServerSideEncryptionByDefault': {'SSEAlgorithm': 'AES256'}}]
        }
    )


def delete(uri):
    pass


bucket_name = '1999-aaa'
create(bucket_name)
