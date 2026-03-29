import unittest
from Favorites_Manager import FavoritesManager

class TestFavoritesManager(unittest.TestCase):

    def setUp(self):
        self.fav = FavoritesManager()

    def test_add_favorite(self):
        self.fav.add_favorite("Freddy Fazbear's Pizza")
        self.assertIn("Freddy Fazbear's Pizza", self.fav.view_favorites())

    def test_prevent_duplicates(self):
        self.fav.add_favorite("Sushi House")
        self.fav.add_favorite("Sushi House")
        self.assertEqual(len(self.fav.view_favorites()), 1)

    def test_remove_favorite(self):
        self.fav.add_favorite("Burger Bar")
        self.fav.remove_favorite("Burger Bar")
        self.assertNotIn("Burger Bar", self.fav.view_favorites())

    def test_view_empty_favorites(self):
        self.assertEqual(len(self.fav.view_favorites()), 0)

    def test_multiple_favorites(self):
        self.fav.add_favorite("Shop A")
        self.fav.add_favorite("Shop B")
        self.assertEqual(len(self.fav.view_favorites()), 2)

    def test_add_empty_favorite(self):
        result = self.fav.add_favorite("")
        self.assertFalse(result)

    def test_remove_non_existing_favorite(self):
        result = self.fav.remove_favorite("NonExistent")
        self.assertFalse(result)

    def test_view_returns_copy(self):
        self.fav.add_favorite("Pizza")
        favs = self.fav.view_favorites()
        favs.append("Fake")
        self.assertNotIn("Fake", self.fav.view_favorites())

if __name__ == "__main__":
    unittest.main()