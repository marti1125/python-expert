import functools


def power(base: float, exponenet: float) -> float:
    return base ** exponenet


def main() -> None:
    square = functools.partial(power, exponenet=2)
    cube = functools.partial(power, exponenet=3)
    print("Square of 5:", square(5))
    print("Cube of 3:", cube(3))


if __name__ == "__main__":
    main()