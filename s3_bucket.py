import boto3


def create_bucket(bucket_name):
    try:
        # Create an S3 client
        s3 = boto3.client('s3')

        # Create a new S3 bucket
        response = s3.create_bucket(
            Bucket=bucket_name,
            CreateBucketConfiguration={
                'LocationConstraint': 'ap-southeast-1'
            }
        )

        # Print the response
        print(response)
    except:
        print('bucket exist')


def upload_to_bucket(bucket_name, file_name, dest_name):
    # Create an S3 client
    s3 = boto3.client('s3')

    # Upload the file to S3
    s3.upload_file(file_name,
                   bucket_name, dest_name)
