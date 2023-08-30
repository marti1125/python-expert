from pathlib import Path
from dataclasses import dataclass
import itertools


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

    for i in itertools.count(10, 5):
        print(i)
        if i == 50:
            break
    
    subtotals = [2, 5, 7, 5, 3, 3]
    for i in itertools.accumulate(subtotals):
        print(i)

    playing_cards: list[str] = [
        "2",
        "3",
        "4",
        "5",
        "6",
        "7",
        "8",
        "9",
        "10",
        "J",
        "Q",
        "K",
        "A",
    ]
    # perms = itertools.permutations(playing_cards, 4)
    # for perm in perms:
    #     print(perm)
    
    perms = itertools.combinations(playing_cards, 4)
    for perm in perms:
        print(perm)
    
    values: list[str] = ["a", "b", "c"]
    cn = itertools.chain(values, ["d", "e", "f"])
    print(list(cn))

    print(list(itertools.filterfalse(lambda x: x.weight < 1, inventory)))

    print(list(itertools.starmap(lambda x, y: x * y, [(2, 6), (8, 4), (5, 3)])))


if __name__ == "__main__":
    main()