import random
import string
from dataclasses import dataclass, field


def generate_id():
    return "".join(random.choices(string.ascii_uppercase, k=12))


@dataclass(kw_only=True)
class Person:
    name: str
    address: str
    id: str = field(default_factory=generate_id, init=False)
    active: bool = True
    email_addresses: list[str] = field(default_factory=list)
    _search_string: str = field(init=False, repr=False)

    def __post_init__(self) -> None:
        self._search_string = f"{self.name} {self.address}"


def main() -> None:
    person = Person(name="John Doe", address="123 Main Street")
    print(person)


if __name__ == "__main__":
    main()
