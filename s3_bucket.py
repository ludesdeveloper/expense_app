import boto3


def upload_to_bucket(bucket_name, file_name, dest_name):
    # Create an S3 client
    s3 = boto3.client('s3')

    # Upload the file to S3
    s3.upload_file(file_name,
                   bucket_name, dest_name)
