import os
from app.utils.s3 import S3Client

def upload():
    try:
        os.makedirs('gen_data', exist_ok=True)
        for root, dirs, files in os.walk('gen_data'):
            for file in files:
                if file.endswith('.csv'):
                    file_path = os.path.join(root, file)
                    try:
                        s3_url = S3Client.upload_file(file_path)
                        print(f'Uploaded {file} to S3: {s3_url}')
                    except Exception as e:
                        print(f'Error uploading {file} to S3: {str(e)}')
        print('All files uploaded to S3')
    except Exception as e:
        print(f'Error creating directory: {str(e)}')