import unittest
from src.data_ingestion.data_loader import DataLoader

class TestDataLoader(unittest.TestCase):
    def test_load_data(self):
        data_loader = DataLoader('data/test_data.csv')
        data = data_loader.load_data()
        self.assertIsNotNone(data)
        self.assertFalse(data.empty)

if __name__ == "__main__":
    unittest.main()
