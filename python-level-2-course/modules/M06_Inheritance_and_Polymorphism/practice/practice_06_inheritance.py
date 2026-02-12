"""Practice: Inheritance and polymorphism (PCAP 4.5).

Implement Shape and Rectangle. Run main() to test.
"""


class Shape:
    """Base shape (PCAP 4.5)."""
    def area(self) -> float:
        return 0.0


class Rectangle(Shape):
    """Rectangle with width and height."""
    def __init__(self, w: float, h: float):
        self.w = w
        self.h = h

    def area(self) -> float:
        return self.w * self.h


def main() -> None:
    r = Rectangle(3, 4)
    print("Rectangle(3, 4).area():", r.area())
    print("isinstance(r, Shape):", isinstance(r, Shape))
    print("isinstance(r, Rectangle):", isinstance(r, Rectangle))


if __name__ == "__main__":
    main()
