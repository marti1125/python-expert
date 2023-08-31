from dataclasses import dataclass
from decimal import Decimal

@dataclass
class Order:
    product: str
    quantity: int
    price: Decimal


def calculate_total_price(quantity: int, price: Decimal) -> Decimal:
    return quantity * price


def main() -> None:
    sales_orders = [
        Order(product="A", quantity=5, price=Decimal("60.00")),
        Order(product="B", quantity=3, price=Decimal("15.00")),
        Order(product="C", quantity=2, price=Decimal("20.00")),
        Order(product="D", quantity=4, price=Decimal("45.00")),
    ]

    # TO DO: Use a generator expression to generate a sequence of total prices for each sales 
    total_prices = (calculate_total_price(order.quantity, order.price) for order in sales_orders)

    # TO DO: Use another generator expression to filter the total prices sequence
    # and keep only the orders with a price greater than $100
    filtered_prices = (price for price in total_prices if price > 100)

    # Print all total prices above $100
    print("Orders larger than $100:")
    for price in filtered_prices:
        print(f" ${price:.2f}")

if __name__ == "__main__":
    main()
