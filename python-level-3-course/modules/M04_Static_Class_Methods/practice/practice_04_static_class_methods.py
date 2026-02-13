"""
PCPP 1.5, 1.6: Practice Exercises - Static/Class Methods & Abstract Classes
"""

import abc


# Exercise 1: Static Methods
# TODO: Create a StringUtils class with static methods:
#   - reverse(s: str) -> str
#   - is_palindrome(s: str) -> bool
#   - capitalize_words(s: str) -> str

class StringUtils:
    """String utility class with static methods."""
    # TODO: Implement static methods
    pass


# Exercise 2: Class Methods as Alternative Constructors
# TODO: Create a Product class with:
#   - __init__(name, price)
#   - @classmethod from_dict(cls, data: dict) -> Product
#   - @classmethod create_discount_product(cls, name, price, discount) -> Product

class Product:
    """Product class with class methods."""
    # TODO: Implement Product class
    pass


# Exercise 3: Abstract Base Class
# TODO: Create an Animal abstract class with:
#   - Abstract method make_sound() -> str
#   - Abstract method move() -> str
#   - Concrete method describe() -> str (uses abstract methods)

class Animal(abc.ABC):
    """Abstract base class for animals."""
    # TODO: Implement abstract class
    pass


# Exercise 4: Concrete Implementations
# TODO: Create Dog and Cat classes inheriting from Animal
#   - Implement all abstract methods
#   - Add class-specific attributes

class Dog(Animal):
    """Dog class."""
    # TODO: Implement
    pass


class Cat(Animal):
    """Cat class."""
    # TODO: Implement
    pass


# Exercise 5: Multiple Inheritance with ABCs
# TODO: Create abstract classes Flyable and Swimmable
#   Create a Duck class that inherits from Animal, Flyable, and Swimmable
#   Implement all abstract methods

class Flyable(abc.ABC):
    """Abstract class for flying capability."""
    # TODO: Implement
    pass


class Swimmable(abc.ABC):
    """Abstract class for swimming capability."""
    # TODO: Implement
    pass


class Duck(Animal, Flyable, Swimmable):
    """Duck class with multiple inheritance."""
    # TODO: Implement
    pass


if __name__ == "__main__":
    print("Complete the exercises above!")
