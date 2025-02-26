import unittest
from src.optimization.route_optimizer import RouteOptimizer

class TestRouteOptimizer(unittest.TestCase):
    def test_optimize_route(self):
        locations = [(34.05, -118.24), (36.16, -115.13), (37.77, -122.41)]
        route_optimizer = RouteOptimizer(locations)
        optimized_route = route_optimizer.optimize_route()
        self.assertEqual(len(optimized_route), len(locations))

if __name__ == "__main__":
    unittest.main()
