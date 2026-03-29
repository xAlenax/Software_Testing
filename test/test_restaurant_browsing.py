# Unit tests for RestaurantBrowsing class
import unittest
from Restaurant_Browsing import RestaurantBrowsing, RestaurantDatabase

class TestRestaurantBrowsing(unittest.TestCase):
    """
    Unit tests for the RestaurantBrowsing class, testing various search functionalities.
    """

    def setUp(self):
        """
        Set up the test case by initializing a RestaurantDatabase and RestaurantBrowsing instance.
        """
        self.database = RestaurantDatabase()
        self.browsing = RestaurantBrowsing(self.database)

    def test_search_by_cuisine(self):
        """
        Test searching for restaurants by cuisine type.
        """
        results = self.browsing.search_by_cuisine("Italian")
        self.assertEqual(len(results), 2)  # There should be 2 Italian restaurants
        self.assertTrue(all([restaurant['cuisine'] == "Italian" for restaurant in results]))  # Check if all returned restaurants are Italian

    def test_search_by_location(self):
        """
        Test searching for restaurants by location.
        """
        results = self.browsing.search_by_location("Downtown")
        self.assertEqual(len(results), 2)  # There should be 2 restaurants located Downtown
        self.assertTrue(all([restaurant['location'] == "Downtown" for restaurant in results]))  # Check if all returned restaurants are in Downtown

    def test_search_by_rating(self):
        """
        Test searching for restaurants by minimum rating.
        """
        results = self.browsing.search_by_rating(4.0)
        self.assertEqual(len(results), 4)  # There should be 4 restaurants with a rating >= 4.0
        self.assertTrue(all([restaurant['rating'] >= 4.0 for restaurant in results]))  # Check if all returned restaurants have a rating >= 4.0

    def test_search_by_filters(self):
        """
        Test searching for restaurants by multiple filters (cuisine type, location, and minimum rating).
        """
        results = self.browsing.search_by_filters(cuisine_type="Italian", location="Downtown", min_rating=4.0)
        self.assertEqual(len(results), 1)  # Only one restaurant should match all the filters
        self.assertEqual(results[0]['name'], "Italian Bistro")  # The result should be "Italian Bistro"

    def test_search_empty_result(self):
        results = self.browsing.search_by_cuisine("Indian")
        self.assertEqual(len(results), 0)

    def test_search_case_insensitive(self):
        results = self.browsing.search_by_cuisine("italian")
        self.assertEqual(len(results), 2)

if __name__ == "__main__":
    unittest.main()