import os
import sys
from zipfile import ZipFile
from logger import *
from configuration.gcloud_syncer import GCloudSync
from entity.config_entity import DataIngestionConfig
from entity.artifact_entity import DataIngestionArtifacts


class DataIngestion:
    def __init__(self, data_ingestion_config:DataIngestionConfig):
        self.data_ingestion_config=data_ingestion_config
        self.gcloud=GCloudSync


    def get_data_from_gcloud(self):
        try:
            logging.info(f"Going for data ingestion")
            os.makedirs(self.data_ingestion_config.DATA_INGESTION_ARTIFACTS_DIR,exist_ok=True)
            self.gcloud.sync_folder_from_gcloud(self.data_ingestion_config.BUCKET_NAME,self.data_ingestion_config.ZIP_FILE_NAME,self.data_ingestion_config.DATA_INGESTION_ARTIFACTS_DIR)
            logging.info(f"Got the data from gcloud")

        except Exception as e:
            raise e


    def unzip_and_clean(self):
        logging.info(f"unzipping the data")

        try:
            with ZipFile(self.data_ingestion_config.ZIP_FILE_DIR,'r') as zip_ref:
                zip_ref.extractall(self.data_ingestion_config.UNZIP_FILE_PATH)
            logging.info(f"Unzip completed")

            return  self.data_ingestion_config.DATA_ARTIFACTS_DIR,self.data_ingestion_config.NEW_DATA_ARTIFACTS_DIR
        
        except Exception as e:
            raise e
        


    def initiate_data_ingestion(self) -> DataIngestionArtifacts:

        try:
            self.get_data_from_gcloud()
            imbalance_data_file_path,raw_data_file_path=self.unzip_and_clean()

            data_ingestion_artifacts=DataIngestionArtifacts(
                raw_data_file_path=raw_data_file_path,
                imbalance_data_file_path=imbalance_data_file_path
                
            )
            return data_ingestion_artifacts
        
        except Exception as e:
            raise e
        
    


    


    
    