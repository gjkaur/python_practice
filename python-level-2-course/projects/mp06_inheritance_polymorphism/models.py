"""Inheritance and polymorphism (PCAP 4.5)."""

class Product:
    def __init__(self, name: str, price: float):
        self.name = name
        self.price = price

    def get_price(self) -> float:
        return self.price

    def __str__(self) -> str:
        return f"{self.name}: {self.price:.2f}"

class DiscountedProduct(Product):
    def __init__(self, name: str, price: float, discount: float):
        super().__init__(name, price)
        self.discount = discount

    def get_price(self) -> float:
        return self.price * (1 - self.discount)

    def __str__(self) -> str:
        return f"{self.name}: {self.get_price():.2f} (discounted)"
