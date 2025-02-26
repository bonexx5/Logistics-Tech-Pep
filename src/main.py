from src.data_ingestion.data_loader import DataLoader
from src.data_processing.data_cleaner import DataCleaner
from src.optimization.route_optimizer import RouteOptimizer
from src.models.delivery_time_predictor import DeliveryTimePredictor
from src.utils.logger import get_logger

logger = get_logger(__name__)

def main():
    try:
        # Load data
        data_loader = DataLoader('data/logistics_data.csv')
        data = data_loader.load_data()

        # Clean data
        data_cleaner = DataCleaner(data)
        cleaned_data = data_cleaner.clean_data()

        # Optimize route
        locations = list(zip(cleaned_data['latitude'], cleaned_data['longitude']))
        route_optimizer = RouteOptimizer(locations)
        optimized_route = route_optimizer.optimize_route()

        # Predict delivery time
        delivery_time_predictor = DeliveryTimePredictor(cleaned_data)
        predictions = delivery_time_predictor.predict_delivery_time()

        logger.info("Pipeline executed successfully")

    except Exception as e:
        logger.error(f"Error in pipeline execution: {e}")

if __name__ == "__main__":
    main()
