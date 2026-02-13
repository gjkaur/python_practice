"""
PCPP 1.7, 1.8: Practice Exercises - Encapsulation & Built-in Subclassing
"""


# Exercise 1: Properties
# TODO: Create a BankAccount class with:
#   - Private _balance attribute
#   - Property balance (read-only getter)
#   - Methods deposit(amount) and withdraw(amount) to modify balance
#   - Validation: balance cannot go negative

class BankAccount:
    """BankAccount class with encapsulation."""
    # TODO: Implement
    pass


# Exercise 2: Property with Setter
# TODO: Create a Person class with:
#   - Private _age attribute
#   - Property age with getter and setter
#   - Setter validates: age must be between 0 and 150

class Person:
    """Person class with age property."""
    # TODO: Implement
    pass


# Exercise 3: Computed Property
# TODO: Create a Rectangle class with:
#   - width and height attributes
#   - Property area (computed, read-only)
#   - Property perimeter (computed, read-only)

class Rectangle:
    """Rectangle with computed properties."""
    # TODO: Implement
    pass


# Exercise 4: Subclassing list
# TODO: Create a SortedList class inheriting from list:
#   - Override append() to maintain sorted order
#   - Override extend() to maintain sorted order
#   - Add method insert_sorted(item) that inserts in correct position

class SortedList(list):
    """List that maintains sorted order."""
    # TODO: Implement
    pass


# Exercise 5: Subclassing dict
# TODO: Create a DefaultDict class inheriting from dict:
#   - Override __getitem__ to return default value if key not found
#   - Accept default_factory in __init__
#   - If default_factory is callable, call it; otherwise return the value

class DefaultDict(dict):
    """Dict with default values."""
    # TODO: Implement
    pass


if __name__ == "__main__":
    print("Complete the exercises above!")
