import s3fs
import pandas as pd

storage_options = {
    "key": "admin",
    "secret": "password12345",
    "client_kwargs": {
        "endpoint_url": "http://localhost:9000"
        }
}

df_from_minio = pd.read_parquet(
    "s3://airport/processed/flights.parquet",
    storage_options=storage_options
)