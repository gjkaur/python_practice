"""Domain models (PCAP 4.1-4.6)."""

class Product:
    def __init__(self, name: str, price: float):
        self.name = name
        self.price = price

    def format_line(self) -> str:
        return f"{self.name}: {self.price:.2f}"

    def __str__(self) -> str:
        return self.format_line()

class OrderLine:
    def __init__(self, product: Product, quantity: int):
        self.product = product
        self.quantity = quantity

    def total(self) -> float:
        return self.product.price * self.quantity
