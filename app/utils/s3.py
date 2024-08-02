import os
import boto3
from app.config import Config

class S3Client:
    s3 = boto3.client('s3',
                      aws_access_key_id=Config.AWS_ACCESS_KEY,
                      aws_secret_access_key=Config.AWS_SECRET_KEY)
    
    @staticmethod
    def upload_file(file_path):
        file_name = os.path.basename(file_path)
        S3Client.s3.upload_file(file_path, Config.S3_BUCKET, file_name)
        return f"s3://{Config.S3_BUCKET}/{file_name}"
    
    @staticmethod
    def download_files(data):
        if os.path.exists('down_data'):
            file_list = os.listdir('down_data')
            for file in file_list:
                file_path = os.path.join('down_data', file)
                os.remove(file_path)
        else:
            os.makedirs('down_data', exist_ok=True)
        files = []
        for key in data['keys']:
            file_path = os.path.join('down_data', os.path.basename(key))
            S3Client.s3.download_file(Config.S3_BUCKET, key, file_path)
            files.append(file_path)
        return files
