import boto3
import os
from botocore.exceptions import ClientError


os.environ['AWS_DEFAULT_REGION'] = 'us-west-2'
client = boto3.client('s3')


def create(uri, cost_code):
    try:
        client.create_bucket(
            Bucket=uri,
            CreateBucketConfiguration={
                'LocationConstraint': os.environ['AWS_DEFAULT_REGION']
            }
        )
    except ClientError as e:
        print(e.response['Error']['Code'])
        if '' == 'BucketAlreadyOwnedByYou':
            pass

    client.put_bucket_encryption(
        Bucket=uri,
        ServerSideEncryptionConfiguration={
            'Rules': [{'ApplyServerSideEncryptionByDefault': {'SSEAlgorithm': 'AES256'}}]
        }
    )

    client.put_public_access_block(
        Bucket=uri,
        PublicAccessBlockConfiguration={
            'BlockPublicAcls': True,
            'IgnorePublicAcls': True,
            'BlockPublicPolicy': True,
            'RestrictPublicBuckets': True
        }
    )


def delete(uri):
    pass


bucket_name = '1999-aaa'
create(bucket_name, 'T001')
