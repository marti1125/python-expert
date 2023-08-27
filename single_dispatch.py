from functools import singledispatch


@singledispatch
def add(x: int, y: int) -> int:
    return x + y


@add.register
def _(x: str, y: str) -> str:
    return f"{x} {y}"


# you can also use the union type
@add.register
def _(x: list | set, y: list | set ) -> list:
    return [*x, *y]


# functional form
add.register(tuple, lambda x, y: (*x, *y))


def main() -> None:
    print(add(1, 2))
    print(add("hello", "world"))
    print(add([1, 2, 3,], [1, 2, 3]))
    print(add({1, 2, 3,}, {1, 2, 3}))
    print(add((1, 2, 3,), (1, 2, 3)))


if __name__ == "__main__":
    main()