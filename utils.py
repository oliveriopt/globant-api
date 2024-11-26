import boto3

def connect_s3(config):
    s3 = boto3.client(
        's3',
        aws_access_key_id=config.S3_ACCESS_KEY,
        aws_secret_access_key=config.S3_SECRET_KEY,
        region_name=config.S3_REGION
    )
    return s3