import itertools
from typing import Iterable, Tuple


def is_prime(n: int) -> bool:
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


def main() -> None:
    # Test data
    data = [1, 2, 3, 4, 5]

    # TODO
    perms: Iterable[Tuple[int, ...]] = list(itertools.permutations(data))
    only_prime: Iterable[Tuple[int, ...]] = list(itertools.filterfalse(lambda x: not is_prime(x[0]), perms))
    chained_permutations: Iterable[int] = list(itertools.chain(*only_prime))

    # Print the sum of the chained permutations
    print("Sum of chained permutations:", sum(chained_permutations))


if __name__ == "__main__":
    main()
