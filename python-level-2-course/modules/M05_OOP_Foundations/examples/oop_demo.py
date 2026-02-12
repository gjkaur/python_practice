"""Demonstrate class, __init__, instance/class vars, __dict__, hasattr (PCAP 4.1-4.4, 4.6)."""

class Account:
    _count = 0  # class variable (PCAP 4.2)

    def __init__(self, name: str, balance: float = 0.0):
        self.name = name
        self.balance = balance
        Account._count += 1

    def deposit(self, amount: float) -> None:
        self.balance += amount

    def __str__(self) -> str:
        return f"Account({self.name!r}, {self.balance})"

# Create objects
a = Account("Alice", 100.0)
a.deposit(50.0)
print(a)
print("a.__dict__ =", a.__dict__)
print("hasattr(a, 'balance') =", hasattr(a, "balance"))
print("Account.__name__ =", Account.__name__)
