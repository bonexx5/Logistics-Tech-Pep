from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from src.utils.logger import get_logger

logger = get_logger(__name__)

class DeliveryTimePredictor:
    def __init__(self, data):
        self.data = data

    def predict_delivery_time(self):
        try:
            # Example: Predict delivery time using RandomForestRegressor
            X = self.data.drop(columns=['delivery_time'])
            y = self.data['delivery_time']
            X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

            model = RandomForestRegressor()
            model.fit(X_train, y_train)
            predictions = model.predict(X_test)

            logger.info("Delivery time predicted successfully")
            return predictions
        except Exception as e:
            logger.error(f"Error predicting delivery time: {e}")
            raise
