import boto3
import pandas as pd

df = pd.read_csv('data/flights.csv')
df.to_parquet(
    "data/flights.parquet",
    index=False)

s3 = boto3.client(
    "s3",
    endpoint_url="http://localhost:9000",
    aws_access_key_id="admin",
    aws_secret_access_key="password12345"
)

s3.upload_file(
    "data/flights.csv",
    "airport",
    "raw/flights.csv"
)

s3.upload_file(
    "data/flights.parquet",
    "airport",
    "processed/flights.parquet"
)

