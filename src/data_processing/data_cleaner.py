import pandas as pd
from src.utils.logger import get_logger

logger = get_logger(__name__)

class DataCleaner:
    def __init__(self, data):
        self.data = data

    def clean_data(self):
        try:
            # Example: Drop missing values
            self.data = self.data.dropna()
            logger.info("Data cleaned successfully")
            return self.data
        except Exception as e:
            logger.error(f"Error cleaning data: {e}")
            raise
