import os
import urllib.request as request
from mlProject import logger
from mlProject.utils.common import get_size
from mlProject.entity.config_entity import DataIngestionConfig
from pathlib import Path

class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config

    def download_file(self):
        if not os.path.exists(self.config.local_data_file):
            filename, headers = request.urlretrieve(
                url = self.config.source_URL,
                filename = self.config.local_data_file
            )
            logger.info(f"{filename} downloaded successfully!")
        else:
            logger.info(f"File already exists with size: {get_size(Path(self.config.local_data_file))}")

    def extract_zip_file(self):
        logger.info("Skipping zip extraction: Dataset downloaded directly as raw CSV file.")
        pass
