import os
import urllib.request as request
import zipfile
from pathlib import Path

from mlProject import logger
from mlProject.entity.config_entity import DataIngestionConfig
from mlProject.utils.common import get_size


class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config

    def download_file(self):
        if not os.path.exists(self.config.local_data_file):
            self.config.local_data_file.parent.mkdir(parents=True, exist_ok=True)
            filename, headers = request.urlretrieve(
                url=self.config.source_URL,
                filename=self.config.local_data_file,
            )
            logger.info(f"{filename} downloaded successfully!")
        else:
            logger.info(
                f"File already exists with size: {get_size(Path(self.config.local_data_file))}"
            )

    def extract_zip_file(self):
        if not os.path.exists(self.config.local_data_file):
            raise FileNotFoundError(f"File not found: {self.config.local_data_file}")

        if not zipfile.is_zipfile(self.config.local_data_file):
            logger.info("Downloaded file is not a zip archive. Skipping extraction.")
            return

        self.config.unzip_dir.mkdir(parents=True, exist_ok=True)
        with zipfile.ZipFile(self.config.local_data_file, "r") as zip_ref:
            zip_ref.extractall(self.config.unzip_dir)

        logger.info(f"Zip archive extracted successfully to: {self.config.unzip_dir}")
