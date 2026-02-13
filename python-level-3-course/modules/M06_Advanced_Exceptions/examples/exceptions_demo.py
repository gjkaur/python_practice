"""
PCPP 1.9, 1.10: Advanced Exceptions & Object Copying Demo
"""

import copy
import traceback
from typing import Any


# PCPP 1.9: Exception Chaining
class DatabaseError(Exception):
    """Custom exception for database errors."""
    pass


class ApplicationError(Exception):
    """Custom exception for application errors."""
    pass


def database_operation() -> None:
    """Simulate database operation that fails."""
    raise DatabaseError("Connection timeout")


def save_user_data() -> None:
    """Save user data with exception chaining."""
    try:
        database_operation()
    except DatabaseError as db_error:
        # PCPP 1.9: Explicit exception chaining
        raise ApplicationError("Failed to save user data") from db_error


# PCPP 1.9: Traceback Objects
def analyze_exception(exc: Exception) -> dict[str, Any]:
    """PCPP 1.9: Analyze exception traceback.
    
    Args:
        exc: Exception object
        
    Returns:
        Dictionary with traceback information
    """
    info = {
        'exception_type': type(exc).__name__,
        'message': str(exc),
        'traceback': None
    }
    
    if exc.__traceback__:
        # PCPP 1.9: Access __traceback__ attribute
        info['traceback'] = traceback.format_tb(exc.__traceback__)
        info['formatted'] = traceback.format_exception(type(exc), exc, exc.__traceback__)
    
    if exc.__cause__:
        info['cause'] = str(exc.__cause__)
    
    if exc.__context__:
        info['context'] = str(exc.__context__)
    
    return info


# PCPP 1.10: Shallow and Deep Copy
class NestedObject:
    """Object with nested mutable attributes."""
    
    def __init__(self, name: str, items: list[str]) -> None:
        self.name = name
        self.items = items
    
    def __repr__(self) -> str:
        return f"NestedObject(name='{self.name}', items={self.items})"


def demonstrate_copying() -> None:
    """PCPP 1.10: Demonstrate shallow vs deep copy."""
    original = NestedObject("Original", ["item1", "item2"])
    
    # Shallow copy
    shallow = copy.copy(original)
    shallow.items.append("item3")
    
    print(f"Original after shallow copy: {original}")
    print(f"Shallow copy: {shallow}")
    print(f"Same items list? {original.items is shallow.items}")
    
    # Deep copy
    original2 = NestedObject("Original2", ["item1", "item2"])
    deep = copy.deepcopy(original2)
    deep.items.append("item3")
    
    print(f"\nOriginal after deep copy: {original2}")
    print(f"Deep copy: {deep}")
    print(f"Same items list? {original2.items is deep.items}")


# PCPP 1.10: Object Identity
def demonstrate_identity() -> None:
    """Demonstrate object identity vs value."""
    a = [1, 2, 3]
    b = a  # Same object (alias)
    c = [1, 2, 3]  # Different object, same value
    
    print(f"a is b: {a is b}")  # True - same identity
    print(f"a is c: {a is c}")  # False - different identity
    print(f"a == c: {a == c}")  # True - same value
    print(f"id(a): {id(a)}")
    print(f"id(b): {id(b)}")
    print(f"id(c): {id(c)}")


if __name__ == "__main__":
    print("=== Exception Chaining ===")
    try:
        save_user_data()
    except ApplicationError as e:
        print(f"Caught: {e}")
        print(f"Caused by: {e.__cause__}")
        print(f"Context: {e.__context__}")
    
    print("\n=== Traceback Analysis ===")
    try:
        raise ValueError("Test error")
    except ValueError as e:
        info = analyze_exception(e)
        print(f"Exception info: {info}")
    
    print("\n=== Object Copying ===")
    demonstrate_copying()
    
    print("\n=== Object Identity ===")
    demonstrate_identity()
