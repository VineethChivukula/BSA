import os
import sys
import boto3
from app.utils.s3 import S3Client
from app.config import Config

def list_s3_files(bucket, year, month):
    try:
        s3 = boto3.client('s3',
                          aws_access_key_id=Config.AWS_ACCESS_KEY,
                          aws_secret_access_key=Config.AWS_SECRET_KEY)
        response = s3.list_objects_v2(Bucket=bucket)
        keys = [content['Key'] for content in response.get('Contents', []) if content['Key'].endswith('.csv')]
        filtered_keys = [key for key in keys if f"_{int(year)}_{int(month):02d}.csv" in key]
        return filtered_keys
    except Exception as e:
        print(f"Error occurred while listing S3 files: {str(e)}")
        return []

def download():
    try:
        year = input("Enter the year for downloading statements: ")
        month = input("Enter the month for downloading statements: ")
        keys = list_s3_files(Config.S3_BUCKET, year, month)
        if keys: 
            data = {'keys': keys}
            S3Client.download_files(data)
            print("Statements have been downloaded.")
            # Save year and month to a temporary file
            with open('temp_config.txt', 'w') as f:
                f.write(f"{year},{month}")
        else:
            print("No statements found in the S3 bucket.")
            sys.exit(1)
    except Exception as e:
        print(f"Error occurred while downloading files: {str(e)}")