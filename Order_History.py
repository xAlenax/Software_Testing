class OrderHistory:
    def __init__(self):
        self.orders = []

    def add_order(self, order_id, items, total, status="Delivered"):
        order = {
            "order_id": order_id,
            "items": items,
            "total": total,
            "status": status
        }
        self.orders.append(order)

    def get_orders(self):
        return self.orders

    def filter_orders(self, status=None):
        if status:
            return [o for o in self.orders if o["status"] == status]
        return self.orders