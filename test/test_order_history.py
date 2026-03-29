import unittest
from Order_History import OrderHistory

class TestOrderHistory(unittest.TestCase):

    def setUp(self):
        self.history = OrderHistory()

    def test_add_order(self):
        self.history.add_order("ORD1", ["Pizza"], 20)
        self.assertEqual(len(self.history.get_orders()), 1)

    def test_empty_history(self):
        self.assertEqual(len(self.history.get_orders()), 0)

    def test_multiple_orders(self):
        self.history.add_order("ORD1", ["Pizza"], 20)
        self.history.add_order("ORD2", ["Burger"], 10)
        self.assertEqual(len(self.history.get_orders()), 2)

    def test_filter_orders(self):
        self.history.add_order("ORD1", ["Pizza"], 20, status="Delivered")
        self.history.add_order("ORD2", ["Burger"], 10, status="Pending")
        result = self.history.filter_orders("Pending")
        self.assertEqual(len(result), 1)

    def test_filter_no_status(self):
        self.history.add_order("ORD1", ["Pizza"], 20)
        result = self.history.filter_orders()
        self.assertEqual(len(result), 1)

    def test_add_invalid_order(self):
        result = self.history.add_order("", [], 0)
        self.assertFalse(result)

if __name__ == "__main__":
    unittest.main()