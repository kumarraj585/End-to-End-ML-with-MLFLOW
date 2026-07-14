import tempfile
import unittest
import zipfile
from pathlib import Path

from mlProject.components.data_ingestion import DataIngestion
from mlProject.entity.config_entity import DataIngestionConfig


class TestDataIngestion(unittest.TestCase):
    def test_extract_zip_file_extracts_archive(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            tmp_path = Path(tmpdir)
            archive_path = tmp_path / "sample.zip"
            extract_dir = tmp_path / "extracted"

            with zipfile.ZipFile(archive_path, "w") as zf:
                zf.writestr("data.csv", "a,b\n1,2\n")

            config = DataIngestionConfig(
                root_dir=tmp_path,
                source_URL="https://example.com/sample.zip",
                local_data_file=archive_path,
                unzip_dir=extract_dir,
            )

            DataIngestion(config).extract_zip_file()

            self.assertTrue((extract_dir / "data.csv").exists())


if __name__ == "__main__":
    unittest.main()
