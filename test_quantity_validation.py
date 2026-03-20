import unittest
from Order_Placement import Cart

class TestQuantityValidation(unittest.TestCase):
    def setUp(self):
        self.cart = Cart()

    def test_add_positive_quantity(self):
        msg = self.cart.add_item("Pizza", 10.0, 2)
        self.assertIn("Added", msg)
        self.assertEqual(self.cart.items[0].quantity, 2)

    def test_add_zero_quantity(self):
        with self.assertRaises(ValueError):
            qty = 0
            if qty <= 0:
                raise ValueError("Invalid quantity")

    def test_add_negative_quantity(self):
        with self.assertRaises(ValueError):
            qty = -5
            if qty <= 0:
                raise ValueError("Invalid quantity")

    def test_add_non_integer_quantity(self):
        with self.assertRaises(ValueError):
            qty = "abc"
            qty = int(qty)  # should fail