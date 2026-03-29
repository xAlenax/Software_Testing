class OrderHistory:
    def __init__(self):
        self.orders = []

    def add_order(self, order_id, items, total, status="Delivered"):
        if not order_id or not items or total <= 0:
            return False

        if any(o["order_id"] == order_id for o in self.orders):
            return False

        order = {
            "order_id": order_id,
            "items": items,
            "total": total,
            "status": status
        }
        self.orders.append(order)
        return True

    def get_orders(self):
        return list(self.orders)

    def filter_orders(self, status=None):
        if status:
            return [o for o in self.orders if o["status"] == status]
        return list(self.orders)