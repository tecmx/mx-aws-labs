import boto3
import os.path
from flask import current_app as app
from werkzeug.utils import secure_filename


def s3_upload(source_file):
    source_filename = secure_filename(source_file.data.filename)
    # Connect to S3 and upload file.
    s3 = boto3.client(
        "s3",
        aws_access_key_id=app.config["AWS_KEY"],
        aws_secret_access_key=app.config["AWS_SECRET"],
        aws_session_token=app.config["AWS_SESSION"]
    )
    s3.put_object(
        Bucket=app.config["S3_BUCKET"],
        Key=source_filename,
        Body=source_file.data
    )
    return source_filename
