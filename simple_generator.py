from typing import Generator


def echo_round() -> Generator[int, float, str]:
    res = yield
    while res:
        res = yield round(res)
    return "OK"


def simple_generator() -> Generator[str, None, None]:
    generator_str = "Hello World"
    yield generator_str
    generator_str += "!"
    yield generator_str


def main() -> None:

    for generator_str in simple_generator():
        print(generator_str)

    print(next(simple_generator()))

    echo = echo_round()
    next(echo)
    print(echo.send(3.2))
    print(echo.send(3.9))
    print(echo.send(10.13))
    print(echo.send(8.2))
    try:
        print(echo.send(0.0))
    except StopIteration as e:
        print(e.value)


if __name__ == "__main__":
    main()