import os

from datetime import datetime

TIMESTAMP: str =datetime.now().strftime("%m_%d_%Y_%H_%S")
ARTIFACTS_DIR=os.pth.join("artifacts",TIMESTAMP)
BUCKET_NAME="hate"
ZIP_FILE_NAME="dataset.zip"
LABEL="label"
TWEET="tweet"


# Data Ingestion Constant:
DATA_INGESTION_ARTIFACTS_DIR="DataIngestionArtifacts"
DATA_INGESTION_IMBALANCE_DATA_DIR="imbalanced_data.csv"
Data_INGESTION_RAW_DATA_DIR="raw_data.csv"

