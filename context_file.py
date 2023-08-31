from typing import Generator, IO, Any 
from contextlib import contextmanager


@contextmanager
def file_manager(file_name: str, mode: str) -> Generator[IO[Any], None, None]:
    try:
        file = open(file=file_name, mode=mode)
        yield file
    finally:
        file.close()


def main() -> None:
    with file_manager("sample.txt", "w") as file:
        file.write("Hello, world!")


if __name__ == "__main__":
    main()