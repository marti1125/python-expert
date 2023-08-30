import itertools
from typing import Collection, Iterable, Tuple


# This function calculates the average of a list of numbers
# Note: I'm using the Collection type hint here, which is a generic type hint
# for collections/iterables that support the len() function.
def calculate_average(numbers: Collection[int]) -> float:
    total = sum(numbers)
    return total / len(numbers)


def main() -> None:
    data = [1, 2, 3, 4, 5]


    combinations: Iterable[Tuple[int, int]] = list(itertools.combinations(data, 2))
    averages: Iterable[int] = list(itertools.starmap(lambda x, y: calculate_average([x, y]), combinations))

    print("Averages of combinations:")
    for average in averages:
        print(average)


if __name__ == "__main__":
    main()
