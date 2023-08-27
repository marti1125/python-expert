from dataclasses import dataclass
from typing import Callable
import functools


@dataclass
class Customer:
    name: str
    age: int


# higher order functions
def send_email_promotion(customers: list[Customer], is_eligible: Callable[[Customer], bool]) -> None:
    for customer in customers:
        print(f"Checking {customer}")
        if is_eligible:
            print(f"{customer.name} is eligible for promotion")
        else:
            print(f"{customer.name} is not eligible for promotion")


def is_eligible_for_promotion(customer: Customer, cutoff_age: int) -> bool:
    return customer.age > cutoff_age


def main() -> None:
    customers = [
        Customer("Alice", 35),
        Customer("Bob", 30),
    ]
    is_eligible_60 = functools.partial(is_eligible_for_promotion, 60)
    send_email_promotion(customers, is_eligible_60)


if __name__ == "__main__":
    main()