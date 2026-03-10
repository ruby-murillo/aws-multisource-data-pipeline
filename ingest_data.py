import boto3

s3 = boto3.client('s3')

bucket_name = "ruby-data-engineering-pipeline-2026"
file_name = "sample_dataset.csv"
s3_key = "raw/sample_dataset.csv"

s3.upload_file(file_name, bucket_name, s3_key)

print("Upload successful")