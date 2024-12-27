
def cancel_order(order_id, orders):
    """Cancel an order if it has not been paid."""
    if order_id not in orders:
        return f"Order with ID {order_id} does not exist."

    order = orders[order_id]

    if order["status"] == "Paid":
        return f"Order {order_id} cannot be canceled as it is already paid."

    if order["status"] == "Pending Payment":
        order["status"] = "Canceled"
        return f"Order {order_id} has been successfully canceled."

