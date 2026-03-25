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


if __name__ == "__main__":
    unittest.main()