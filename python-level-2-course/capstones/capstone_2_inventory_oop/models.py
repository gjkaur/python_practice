"""Item model (PCAP 4.x)."""

class Item:
    def __init__(self, item_id: str, name: str, quantity: int, price: float):
        self.id = item_id
        self.name = name
        self.quantity = quantity
        self.price = price

    def __str__(self) -> str:
        return f"{self.id} {self.name} qty={self.quantity} price={self.price:.2f}"

    def to_dict(self) -> dict:
        return {"id": self.id, "name": self.name, "quantity": self.quantity, "price": self.price}

    @classmethod
    def from_dict(cls, d: dict) -> "Item":
        return cls(d["id"], d["name"], d["quantity"], d["price"])
