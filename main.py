
from database import orders
from operation import cancel_order

if __name__ == "__main__":
    print("Available Orders:")
    for order_id, order_info in orders.items():
        print(f"Order ID: {order_id}, Status: {order_info['status']}, Total: {order_info['total']}")

    order_to_cancel = int(input("Enter the ID of the order you want to cancel: "))
    result = cancel_order(order_to_cancel, orders)
    print(result)

    print("\nUpdated Orders:")
    for order_id, order_info in orders.items():
        print(f"Order ID: {order_id}, Status: {order_info['status']}, Total: {order_info['total']}")
