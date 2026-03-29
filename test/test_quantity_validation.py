import unittest
from Order_Placement import Cart
from Validators import validate_quantity

class TestQuantityValidation(unittest.TestCase):
    def setUp(self):
        self.cart = Cart()

    def test_add_positive_quantity(self):
        msg = self.cart.add_item("Pizza", 10.0, 2)
        self.assertIn("Added", msg)
        self.assertEqual(self.cart.items[0].quantity, 2)

    def test_validate_quantity_zero(self):
        with self.assertRaises(ValueError):
            validate_quantity("0")

    def test_validate_quantity_negative(self):
        with self.assertRaises(ValueError):
            validate_quantity("-5")

    def test_validate_quantity_non_integer(self):
        with self.assertRaises(ValueError):
            validate_quantity("abc")

if __name__ == "__main__":
    unittest.main()