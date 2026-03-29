class FavoritesManager:
    def __init__(self):
        self.favorites = []

    def add_favorite(self, restaurant):
        """Adds a restaurant if not already in favorites."""
        if restaurant and restaurant not in self.favorites:
            self.favorites.append(restaurant)
            return True
        return False

    def remove_favorite(self, restaurant):
        """Removes a restaurant if it exists."""
        if restaurant in self.favorites:
            self.favorites.remove(restaurant)
            return True
        return False

    def view_favorites(self):
        """Returns a copy of the favorites list."""
        return list(self.favorites)