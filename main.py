from app import create_app

from scripts.generate_transactions import generate
from scripts.upload_to_s3 import upload
from scripts.download_from_s3 import download
from scripts.update_database import update
from scripts.aggregate_statements import aggregate

app = create_app()

if __name__ == '__main__':
    with app.app_context():
        generate()
        upload()
        download()
        update()
        aggregate()
    app.run()
