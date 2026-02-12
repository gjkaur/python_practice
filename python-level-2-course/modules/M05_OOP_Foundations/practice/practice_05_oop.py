"""Practice: OOP foundations (PCAP 4.1-4.4, 4.6).

Implement the class and functions below. Run main() to test.
"""


# --- Task 1: Product class (PCAP 4.1, 4.3, 4.6) ---
class Product:
    """A product with name and price."""

    def __init__(self, name: str, price: float):
        self.name = name
        self.price = price

    def get_info(self) -> str:
        """Return a string like 'name: price'."""
        return f"{self.name}: {self.price}"


# --- Task 2: Class variable (PCAP 4.2) ---
class Counter:
    """A counter with a class-level count of instances created."""

    count = 0

    def __init__(self):
        Counter.count += 1
        self.id = Counter.count


# --- Task 3: hasattr and __dict__ (PCAP 4.4, 4.2) ---
def has_attributes(obj: object, *names: str) -> list[bool]:
    """Return a list of booleans: hasattr(obj, name) for each name."""
    return [hasattr(obj, n) for n in names]


def main() -> None:
    p = Product("Widget", 9.99)
    print(p.get_info())
    print("hasattr(p, 'price'):", hasattr(p, "price"))
    print("p.__dict__:", p.__dict__)

    c1, c2 = Counter(), Counter()
    print("Counter.count:", Counter.count, "c1.id:", c1.id, "c2.id:", c2.id)
    print("has_attributes(p, 'name', 'price', 'x'):", has_attributes(p, "name", "price", "x"))


if __name__ == "__main__":
    main()
