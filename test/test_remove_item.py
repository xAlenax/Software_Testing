import unittest
from Order_Placement import Cart

class TestRemoveItem(unittest.TestCase):

    def setUp(self):
        self.cart = Cart()
        self.cart.add_item("Pizza", 10.0, 2)
        self.cart.add_item("Burger", 8.0, 1)

    def test_remove_existing_item(self):
        msg = self.cart.remove_item("Pizza")
        self.assertIn("Removed", msg)
        self.assertEqual(len(self.cart.items), 1)
        self.assertEqual(self.cart.items[0].name, "Burger")

    def test_remove_non_existing_item(self):
        msg = self.cart.remove_item("Pasta")
        self.assertEqual(len(self.cart.items), 2)

    def test_remove_from_empty_cart(self):
        cart = Cart()
        msg = cart.remove_item("Pizza")
        self.assertEqual(msg, "Removed Pizza from cart")
        self.assertEqual(len(cart.items), 0)

if __name__ == "__main__":
    unittest.main()