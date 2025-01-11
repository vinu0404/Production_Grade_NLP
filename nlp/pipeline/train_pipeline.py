import os
import sys
from logger import *
from configuration.gcloud_syncer import GCloudSync
from entity.config_entity import DataIngestionConfig
from entity.artifact_entity import DataIngestionArtifacts
from components.data_ingestion import DataIngestion


class TrainPipeline:
    def __init__(self):
        self.data_ingestion_config=DataIngestionConfig



    def start_data_ingestion(self) ->DataIngestionArtifacts:
        try:
            data_ingestion=DataIngestion(data_ingestion_config=self.data_ingestion_config)
            data_ingestion_artifacts=data_ingestion.initiate_data_ingestion()
            return data_ingestion_artifacts
        
        except Exception as e:
            raise e
        







    def run_pipeline(self):
        
        try:
            data_ingestion=self.start_data_ingestion()

        except Exception as e:
            raise e
    


           
        















