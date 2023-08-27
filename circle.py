import math
from dataclasses import dataclass


@dataclass
class Circle:
    _radius: float

    @property
    def radius(self) -> float:
        return self._radius

    @radius.setter
    def radius(self, value: float) -> None:
        if value <= 0:
            raise ValueError("Radius must be more than 0")
        self._radius = value
    
    def __post_init__(self) -> None:
        if self._radius <= 0:
            raise ValueError("Radius must be more than 0")
    
    @property
    def diameter(self) -> float:
        return 2 * self._radius
    
    @property
    def area(self) -> float:
        return math.pi * math.pow(self._radius, 2)
    
    @property
    def circumference(self) -> float:
        return 2 * math.pi * self._radius


def main() -> None:
    circle = Circle(-15)
    print("Radius:", circle.radius)
    circle.radius = 10
    print("Diameter:", circle.diameter)
    print("Area:", circle.area)
    print("Circumference:", circle.circumference)


if __name__ == "__main__":
    main()
