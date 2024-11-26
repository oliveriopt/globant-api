import boto3
from config import Config
import pandas as pd

def connect_s3(config) -> object:
    """
    Connect s3
    """
    s3 = boto3.client(
        's3',
        aws_access_key_id=config.S3_ACCESS_KEY,
        aws_secret_access_key=config.S3_SECRET_KEY,
        region_name=config.S3_REGION
    )
    return s3

def fetch_csv_from_s3(s3, bucket_name, folder) -> list:
    """
    Fetch data from s3
    """
    response = s3.list_objects_v2(Bucket=bucket_name, Prefix=folder)
    file_paths = [content['Key'] for content in response.get('Contents', [])]
    
    dataframes = []
    for path in file_paths:
        obj = s3.get_object(Bucket=bucket_name, Key=path)
        data = pd.read_csv(obj['Body'])
        dataframes.append(data)
    return dataframes