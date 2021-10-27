import logging
import boto3
from botocore.exceptions import ClientError
import os

# import requests    # To install: pip install requests

def upload_file(file_name, bucket, object_name=None):
    """Upload a file to an S3 bucket

    :param file_name: File to upload
    :param bucket: Bucket to upload to
    :param object_name: S3 object name. If not specified then file_name is used
    :return: True if file was uploaded, else False
    """

    # If S3 object_name was not specified, use file_name
    if object_name is None:
        object_name = os.path.basename(file_name)

    # Upload the file
    s3_client = boto3.client('s3')
    try:
        s3_client.upload_file(file_name, bucket, object_name)
    except ClientError as e:
        logging.error(e)
        return False
    return True


def create_presigned_url(bucket_name, object_name, expiration=None):
    """Generate a presigned URL to share an S3 object

    :param bucket_name: string
    :param object_name: string
    :param expiration: Time in seconds for the presigned URL to remain valid
    :return: Presigned URL as string. If error, returns None.
    """

    # Generate a presigned URL for the S3 object
    s3_client = boto3.client('s3')
    try:
        response = s3_client.generate_presigned_url('get_object',
                                                    Params={'Bucket': bucket_name,
                                                            'Key': object_name},
                                                    ExpiresIn=expiration)
    except ClientError as e:
        logging.error(e)
        return None

    # The response contains the presigned URL
    return response



s3 = boto3.client('s3')
response = s3.list_buckets()

breakpoint()
# Output the bucket names
print("response", response['Buckets'])
print('Existing buckets:')
for bucket in response['Buckets']:
    print(f'  {bucket["Name"]}')

url_response = create_presigned_url("sharebnb-dnd","testFile.jpeg")
print(url_response, "response from create url")

# if url_response is not None:
#     url = requests.get(url_response)
#     print(url)
    