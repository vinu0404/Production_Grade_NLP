from dataclasses import dataclass

@dataclass
class DataIngestionArtifacts:
    raw_data_file_path: str
    imbalance_data_file_path:str

    
