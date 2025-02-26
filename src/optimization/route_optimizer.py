from geopy.distance import geodesic
from src.utils.logger import get_logger

logger = get_logger(__name__)

class RouteOptimizer:
    def __init__(self, locations):
        self.locations = locations

    def optimize_route(self):
        try:
            # Example: Simple route optimization using nearest neighbor
            optimized_route = []
            current_location = self.locations[0]
            optimized_route.append(current_location)
            remaining_locations = self.locations[1:]

            while remaining_locations:
                next_location = min(remaining_locations, key=lambda loc: geodesic(current_location, loc).km)
                optimized_route.append(next_location)
                remaining_locations.remove(next_location)
                current_location = next_location

            logger.info("Route optimized successfully")
            return optimized_route
        except Exception as e:
            logger.error(f"Error optimizing route: {e}")
            raise
