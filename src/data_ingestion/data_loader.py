import pandas as pd
from src.utils.logger import get_logger

logger = get_logger(__name__)

class DataLoader:
    def __init__(self, file_path):
        self.file_path = file_path

    def load_data(self):
        try:
            data = pd.read_csv(self.file_path)
            logger.info(f"Data loaded successfully from {self.file_path}")
            return data
        except Exception as e:
            logger.error(f"Error loading data: {e}")
            raise
