"""Expense model (PCAP 4.x)."""

class Expense:
    def __init__(self, amount: float, category: str, date: str, description: str = ""):
        self.amount = amount
        self.category = category
        self.date = date
        self.description = description

    def __str__(self) -> str:
        return f"{self.date} {self.category} {self.amount:.2f} {self.description}"

    def to_dict(self) -> dict:
        return {
            "amount": self.amount,
            "category": self.category,
            "date": self.date,
            "description": self.description,
        }

    @classmethod
    def from_dict(cls, d: dict) -> "Expense":
        return cls(
            d["amount"],
            d["category"],
            d["date"],
            d.get("description", ""),
        )
