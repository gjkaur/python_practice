"""
MP04: Encapsulated Class Design

PCPP Objectives: 1.7, 1.8

Implement classes with encapsulation and built-in subclassing.
"""


# TODO: Create class with properties (getter, setter, deleter)
class BankAccount:
    """BankAccount with encapsulated balance."""
    # TODO: Implement with property for balance
    # Setter should validate: balance >= 0
    # Deleter should handle cleanup
    pass


# TODO: Subclass a built-in class
class UniqueList(list):
    """List subclass that prevents duplicates."""
    # TODO: Override append() and extend()
    # Prevent duplicate items
    pass


# TODO: Create another encapsulated class
class Temperature:
    """Temperature with property validation."""
    # TODO: Implement celsius property
    # Setter validates: >= -273.15 (absolute zero)
    # Computed property for fahrenheit (read-only)
    pass
