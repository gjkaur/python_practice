"""
PCPP 1.2: Practice Exercises - Magic Methods

Complete the exercises below to practice magic methods.
"""

from functools import total_ordering
from typing import Any


# Exercise 1: Comparison Methods
# TODO: Create a Student class with:
#   - Instance variables: name, grade (float)
#   - __eq__: compare by name
#   - __lt__: compare by grade (higher grade is "less" for sorting)
#   - Use @total_ordering decorator
#   - __str__ and __repr__ methods

@total_ordering
class Student:
    """Student class for comparison exercises."""
    # TODO: Implement Student class
    
    pass


# Exercise 2: Numeric Methods
# TODO: Create a Money class with:
#   - Instance variables: amount (float), currency (str)
#   - __add__: add Money objects (same currency only)
#   - __sub__: subtract Money objects
#   - __mul__: multiply by scalar (int/float)
#   - __abs__: return absolute value
#   - Raise ValueError if currencies don't match

class Money:
    """Money class for numeric operations."""
    # TODO: Implement Money class
    
    pass


# Exercise 3: Type Conversion
# TODO: Create a Temperature class with:
#   - Instance variable: celsius (float)
#   - __float__: return temperature as float
#   - __int__: return temperature as int (rounded)
#   - __str__: return "X°C"
#   - __repr__: return "Temperature(celsius=X)"
#   - __bool__: return True if temperature > 0

class Temperature:
    """Temperature class for type conversion."""
    # TODO: Implement Temperature class
    
    pass


# Exercise 4: Container Methods
# TODO: Create a ShoppingCart class with:
#   - Internal list of items (strings)
#   - __getitem__: access items by index
#   - __setitem__: modify items by index
#   - __len__: return number of items
#   - __contains__: check if item is in cart
#   - __iter__: iterate over items
#   - __str__: return "ShoppingCart(X items)"

class ShoppingCart:
    """ShoppingCart class for container methods."""
    # TODO: Implement ShoppingCart class
    
    pass


# Exercise 5: Attribute Access
# TODO: Create a DynamicObject class with:
#   - __getattr__: return attribute name as string if not found
#   - __setattr__: store all attributes in internal dict
#   - Prevent infinite recursion

class DynamicObject:
    """DynamicObject class for attribute access."""
    # TODO: Implement DynamicObject class
    
    pass


# Exercise 6: Hashable Objects
# TODO: Modify Student class to be hashable:
#   - Implement __hash__ method
#   - Ensure __eq__ is properly defined
#   - Test: students can be used as dictionary keys

# TODO: Add __hash__ to Student class above


if __name__ == "__main__":
    print("Complete the exercises above!")
    
    # Test your implementations:
    # s1 = Student("Alice", 85.5)
    # s2 = Student("Bob", 90.0)
    # print(s1 < s2)
    # 
    # m1 = Money(100, "USD")
    # m2 = Money(50, "USD")
    # print(m1 + m2)
    # 
    # temp = Temperature(25.5)
    # print(float(temp))
    # print(int(temp))
    # 
    # cart = ShoppingCart(["apple", "banana"])
    # print(len(cart))
    # print("apple" in cart)
    # 
    # obj = DynamicObject()
    # obj.anything = "value"
    # print(obj.anything)
