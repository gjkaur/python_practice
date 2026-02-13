"""
PCPP 1.11, 1.12: Serialization & Metaprogramming Demo
"""

import pickle
import shelve
from typing import Any


# PCPP 1.11: Pickle Module
class Person:
    """Person class for pickling demonstration."""
    
    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
    
    def __repr__(self) -> str:
        return f"Person(name='{self.name}', age={self.age})"


def demonstrate_pickle() -> None:
    """PCPP 1.11: Demonstrate pickle serialization."""
    person = Person("Alice", 30)
    
    # Serialize to bytes
    data = pickle.dumps(person)
    print(f"Pickled data (bytes): {data[:50]}...")
    
    # Deserialize from bytes
    restored = pickle.loads(data)
    print(f"Restored: {restored}")
    
    # Serialize to file
    with open("person.pkl", "wb") as f:
        pickle.dump(person, f)
    
    # Deserialize from file
    with open("person.pkl", "rb") as f:
        loaded = pickle.load(f)
    print(f"Loaded from file: {loaded}")


# PCPP 1.11: Shelve Module
def demonstrate_shelve() -> None:
    """PCPP 1.11: Demonstrate shelve persistent storage."""
    # Create shelve database
    with shelve.open("data.db", flag='c') as db:
        db['users'] = [Person("Alice", 30), Person("Bob", 25)]
        db['settings'] = {'theme': 'dark', 'language': 'en'}
    
    # Read from shelve
    with shelve.open("data.db", flag='r') as db:
        users = db['users']
        settings = db['settings']
        print(f"Users: {users}")
        print(f"Settings: {settings}")


# PCPP 1.12: Metaclasses
class RegistryMeta(type):
    """PCPP 1.12: Metaclass that registers all classes."""
    
    registry: dict[str, type] = {}
    
    def __new__(mcs, name: str, bases: tuple, namespace: dict) -> type:
        """Create class and register it."""
        cls = super().__new__(mcs, name, bases, namespace)
        mcs.registry[name] = cls
        return cls


class RegisteredClass(metaclass=RegistryMeta):
    """Class using RegistryMeta metaclass."""
    pass


# PCPP 1.12: Dynamic Class Creation
def create_class_dynamically() -> None:
    """PCPP 1.12: Create class using type() function."""
    # type(name, bases, dict)
    DynamicClass = type('DynamicClass', (object,), {
        'x': 10,
        'get_x': lambda self: self.x
    })
    
    obj = DynamicClass()
    print(f"Dynamic object: {obj.get_x()}")


# PCPP 1.12: Special Attributes
def inspect_class(cls: type) -> None:
    """PCPP 1.12: Inspect class using special attributes."""
    print(f"Class name: {cls.__name__}")
    print(f"Module: {cls.__module__}")
    print(f"Bases: {cls.__bases__}")
    print(f"MRO: {cls.__mro__}")
    print(f"Dict keys: {list(cls.__dict__.keys())}")


if __name__ == "__main__":
    print("=== Pickle ===")
    demonstrate_pickle()
    
    print("\n=== Shelve ===")
    demonstrate_shelve()
    
    print("\n=== Metaclasses ===")
    print(f"Registry: {RegistryMeta.registry}")
    
    print("\n=== Dynamic Creation ===")
    create_class_dynamically()
    
    print("\n=== Special Attributes ===")
    inspect_class(Person)
