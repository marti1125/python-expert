from pathlib import Path
import os
from dataclasses import dataclass


@dataclass
class Item:
    name: str
    weight: float


def main() -> None:
    inventory = [
        Item("laptop", 1.5),
        Item("phone", 0.5),
        Item("book", 1.0),
        Item("camera", 1.0),
        Item("headphones", 0.5),
        Item("charger", 0.5),
    ]

    # inventory_iterator = iter(inventory)  # inventory.__iter__()
    # print(inventory_iterator.__next__())
    for item in inventory:
        print(item)

    path = os.path.join(Path.cwd(), "countries.txt")

    with open(path) as file:
        for line in iter(file.readline, ""):
            print(line, end="")


if __name__ == "__main__":
    main()