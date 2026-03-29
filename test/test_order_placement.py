import unittest
from unittest import mock
from Order_Placement import OrderPlacement, RestaurantMenu, UserProfile, Cart, PaymentMethod

# Unit tests for OrderPlacement class
class TestOrderPlacement(unittest.TestCase):
    """
    Unit tests for the OrderPlacement class.
    """
    def setUp(self):
        """
        Sets up the test environment by creating instances of necessary classes.
        """
        self.restaurant_menu = RestaurantMenu(available_items=["Burger", "Pizza", "Salad"])
        self.user_profile = UserProfile(delivery_address="123 Main St")
        self.cart = Cart()
        self.order = OrderPlacement(self.cart, self.user_profile, self.restaurant_menu)

    def test_validate_order_empty_cart(self):
        """
        Test case for validating an order with an empty cart.
        """
        result = self.order.validate_order()
        self.assertFalse(result["success"])
        self.assertEqual(result["message"], "Cart is empty")

    def test_validate_order_item_not_available(self):
        """
        Test case for validating an order with an unavailable item.
        """
        self.cart.add_item("Pasta", 15.99, 1)
        result = self.order.validate_order()
        self.assertFalse(result["success"])
        self.assertEqual(result["message"], "Pasta is not available")

    def test_validate_order_success(self):
        """
        Test case for successfully validating an order.
        """
        self.cart.add_item("Burger", 8.99, 2)
        result = self.order.validate_order()
        self.assertTrue(result["success"])
        self.assertEqual(result["message"], "Order is valid")

    def test_confirm_order_success(self):
        """
        Test case for confirming an order with successful payment.
        """
        self.cart.add_item("Pizza", 12.99, 1)
        payment_method = PaymentMethod()
        result = self.order.confirm_order(payment_method)
        self.assertTrue(result["success"])
        self.assertEqual(result["message"], "Order confirmed")
        self.assertEqual(result["order_id"], "ORD123456")

    def test_confirm_order_failed_payment(self):
        """
        Test case for confirming an order with failed payment.
        """
        self.cart.add_item("Pizza", 12.99, 1)
        payment_method = PaymentMethod()

        # Use unittest.mock.patch to simulate failed payment processing.
        with mock.patch.object(payment_method, 'process_payment', return_value=False):
            result = self.order.confirm_order(payment_method)
            self.assertFalse(result["success"])
            self.assertEqual(result["message"], "Payment failed")

    def test_proceed_to_checkout(self):
        """
        Test proceed_to_checkout returns expected totals and address.
        """
        self.cart.add_item("Burger", 8.00, 2)
        checkout_info = self.order.proceed_to_checkout()

        self.assertEqual(checkout_info["delivery_address"], "123 Main St")
        self.assertIn("total_info", checkout_info)
        self.assertAlmostEqual(checkout_info["total_info"]["subtotal"], 16.00)
        self.assertAlmostEqual(checkout_info["total_info"]["tax"], 1.60)
        self.assertAlmostEqual(checkout_info["total_info"]["delivery_fee"], 5.00)

    def test_confirm_order_invalid_cart(self):
        payment_method = PaymentMethod()
        result = self.order.confirm_order(payment_method)
        self.assertFalse(result["success"])

    def test_promo_code_applied(self):
        self.cart.add_item("Pizza", 10, 1)
        payment_method = PaymentMethod()
        result = self.order.confirm_order(payment_method, promo_code="DISCOUNT10")
        self.assertTrue(result["success"])
        self.assertGreater(result["discount_applied"], 0)

if __name__ == "__main__":
    unittest.main()