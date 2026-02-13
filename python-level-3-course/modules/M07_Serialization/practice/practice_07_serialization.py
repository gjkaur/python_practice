"""
PCPP 1.11, 1.12: Practice Exercises - Serialization & Metaprogramming
"""

import pickle
import shelve


# Exercise 1: Pickle Custom Objects
# TODO: Create a class with nested objects (lists, dicts, other custom objects)
#   Serialize and deserialize it using pickle
#   Verify all nested objects are restored correctly

class ComplexObject:
    """Object with nested structures."""
    # TODO: Implement
    pass


# Exercise 2: Shelve Database
# TODO: Create a simple database using shelve:
#   - Store user data (name, email, preferences)
#   - Implement functions: save_user(), get_user(), list_users()
#   - Handle missing keys appropriately

def save_user(user_id: str, user_data: dict) -> None:
    """Save user to shelve database."""
    # TODO: Implement
    pass


def get_user(user_id: str) -> dict | None:
    """Get user from shelve database."""
    # TODO: Implement
    pass


# Exercise 3: Dynamic Class Creation
# TODO: Use type() to create a class dynamically:
#   - Class name: "Calculator"
#   - Methods: add, subtract, multiply, divide
#   - Create instance and test methods

# TODO: Create Calculator class using type()


# Exercise 4: Metaclass
# TODO: Create a metaclass that:
#   - Adds a 'created_at' attribute to all classes
#   - Stores creation timestamp
#   - Create a class using this metaclass

class TimestampMeta(type):
    """Metaclass that adds creation timestamp."""
    # TODO: Implement
    pass


# Exercise 5: Class Inspection
# TODO: Write a function that:
#   - Takes a class as argument
#   - Prints all special attributes (__name__, __bases__, __dict__, etc.)
#   - Lists all methods and attributes

def inspect_class(cls: type) -> None:
    """Inspect a class and print its attributes."""
    # TODO: Implement
    pass


if __name__ == "__main__":
    print("Complete the exercises above!")
