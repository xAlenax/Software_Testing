import unittest
from Order_Placement import PromoCodeManager

class TestPromoCodeManager(unittest.TestCase):

    def setUp(self):
        self.manager = PromoCodeManager()

    def test_apply_valid_promo_code(self):
        discount = self.manager.apply_promo_code("DISCOUNT10", 100.0)
        self.assertEqual(discount, 10.0)

    def test_apply_invalid_promo_code(self):
        discount = self.manager.apply_promo_code("INVALID", 100.0)
        self.assertEqual(discount, 0.0)

    def test_apply_promo_code_case_insensitive(self):
        discount = self.manager.apply_promo_code("discount10", 100.0)
        self.assertEqual(discount, 10.0)

    def test_apply_promo_code_percent_based(self):
        discount = self.manager.apply_promo_code("DISCOUNT10", 200.0)
        self.assertEqual(discount, 20.0)

    def test_apply_promo_code_fixed_amount(self):
        discount = self.manager.apply_promo_code("SAVE5", 30.0)
        self.assertEqual(discount, 5.0)

    def test_apply_promo_code_fixed_amount_cannot_exceed_subtotal(self):
        discount = self.manager.apply_promo_code("SAVE5", 3.0)
        self.assertEqual(discount, 3.0)

    def test_promo_code_once_per_order(self):
        discount1 = self.manager.apply_promo_code("DISCOUNT10", 100.0)
        discount2 = self.manager.apply_promo_code("DISCOUNT10", 100.0)
        self.assertEqual(discount1, 10.0)
        self.assertEqual(discount2, 10.0)

if __name__ == "__main__":
    unittest.main()