"""
MP03: Abstract Base Class Framework

PCPP Objectives: 1.5, 1.6

Implement abstract base classes and concrete implementations.
"""

import abc
from typing import Tuple


# TODO: Define abstract base classes
# Example: Drawable, Movable, or your own domain

class Drawable(abc.ABC):
    """Abstract base class for drawable objects."""
    # TODO: Implement with abstract methods
    pass


class Movable(abc.ABC):
    """Abstract base class for movable objects."""
    # TODO: Implement with abstract methods
    pass


# TODO: Create concrete implementations
class Rectangle(Drawable):
    """Concrete implementation of Drawable."""
    # TODO: Implement
    pass


class Circle(Drawable, Movable):
    """Concrete implementation with multiple inheritance."""
    # TODO: Implement all abstract methods
    pass


# TODO: Add factory methods using @classmethod
# TODO: Add utility methods using @staticmethod
