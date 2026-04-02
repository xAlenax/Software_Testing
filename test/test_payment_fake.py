import unittest
from Order_Placement import OrderPlacement, Cart, UserProfile, RestaurantMenu


class FakePaymentMethod:
    """A fake payment gateway with internal state."""
    def __init__(self):
        self.total_charged = 0

    def process_payment(self, amount):
        self.total_charged += amount
        return True


class TestPaymentProcessingFake(unittest.TestCase):

    def test_fake_payment_gateway(self):
        cart = Cart()
        cart.add_item("Burger", 8.0, 2)

        user = UserProfile("Fake Street 99")
        menu = RestaurantMenu(["Burger"])

        order = OrderPlacement(cart, user, menu)

        fake_payment = FakePaymentMethod()

        result = order.confirm_order(fake_payment)

        self.assertTrue(result["success"])
        self.assertGreater(fake_payment.total_charged, 0)
