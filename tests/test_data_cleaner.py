import unittest
import pandas as pd
from src.data_processing.data_cleaner import DataCleaner

class TestDataCleaner(unittest.TestCase):
    def test_clean_data(self):
        data = pd.DataFrame({
            'latitude': [34.05, 36.16, None],
            'longitude': [-118.24, -115.13, -117.15],
            'delivery_time': [30, 45, 60]
        })
        data_cleaner = DataCleaner(data)
        cleaned_data = data_cleaner.clean_data()
        self.assertFalse(cleaned_data.isnull().values.any())

if __name__ == "__main__":
    unittest.main()
