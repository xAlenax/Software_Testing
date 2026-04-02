import unittest
from unittest.mock import Mock
from Order_Placement import OrderPlacement, Cart, UserProfile, RestaurantMenu


class TestOrderPlacementMock(unittest.TestCase):

    def test_confirm_order_uses_mocked_payment(self):
        # Create cart, user, menu
        cart = Cart()
        cart.add_item("Pizza", 10.0, 1)

        user = UserProfile("Test Street 123")
        menu = RestaurantMenu(["Pizza"])

        order = OrderPlacement(cart, user, menu)

        # Create a mock payment method
        mock_payment = Mock()
        mock_payment.process_payment.return_value = True

        result = order.confirm_order(mock_payment)

        mock_payment.process_payment.assert_called_once()
        self.assertTrue(result["success"])
