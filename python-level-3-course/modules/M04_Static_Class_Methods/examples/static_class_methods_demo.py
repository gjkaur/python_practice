"""
PCPP 1.5, 1.6: Static/Class Methods & Abstract Classes Demo
"""

import abc
from typing import Optional


# PCPP 1.5: Static and Class Methods
class MathUtils:
    """Class demonstrating static methods."""
    
    @staticmethod
    def add(a: float, b: float) -> float:
        """PCPP 1.5: Static method - utility function."""
        return a + b
    
    @staticmethod
    def multiply(a: float, b: float) -> float:
        """Static method for multiplication."""
        return a * b


class Date:
    """Date class demonstrating class methods as alternative constructors."""
    
    def __init__(self, year: int, month: int, day: int) -> None:
        """Initialize Date."""
        self.year = year
        self.month = month
        self.day = day
    
    @classmethod
    def from_string(cls, date_string: str) -> 'Date':
        """PCPP 1.5: Class method - alternative constructor."""
        parts = date_string.split('-')
        return cls(int(parts[0]), int(parts[1]), int(parts[2]))
    
    @classmethod
    def today(cls) -> 'Date':
        """Class method - factory method."""
        from datetime import date
        today = date.today()
        return cls(today.year, today.month, today.day)
    
    def __str__(self) -> str:
        return f"{self.year}-{self.month:02d}-{self.day:02d}"


# PCPP 1.6: Abstract Base Classes
class Shape(abc.ABC):
    """PCPP 1.6: Abstract base class for shapes."""
    
    @abc.abstractmethod
    def area(self) -> float:
        """PCPP 1.6: Abstract method - must be implemented by subclasses."""
        pass
    
    @abc.abstractmethod
    def perimeter(self) -> float:
        """Abstract method for perimeter."""
        pass
    
    def describe(self) -> str:
        """Concrete method - can be used by all subclasses."""
        return f"Shape with area {self.area():.2f} and perimeter {self.perimeter():.2f}"


class Rectangle(Shape):
    """Concrete implementation of Shape."""
    
    def __init__(self, width: float, height: float) -> None:
        self.width = width
        self.height = height
    
    def area(self) -> float:
        """Implement abstract method."""
        return self.width * self.height
    
    def perimeter(self) -> float:
        """Implement abstract method."""
        return 2 * (self.width + self.height)


class Circle(Shape):
    """Concrete implementation of Shape."""
    
    def __init__(self, radius: float) -> None:
        self.radius = radius
    
    def area(self) -> float:
        """Implement abstract method."""
        import math
        return math.pi * self.radius ** 2
    
    def perimeter(self) -> float:
        """Implement abstract method."""
        import math
        return 2 * math.pi * self.radius


# PCPP 1.6: Multiple Inheritance with Abstract Classes
class Drawable(abc.ABC):
    """Abstract class for drawable objects."""
    
    @abc.abstractmethod
    def draw(self) -> str:
        """Abstract method for drawing."""
        pass


class Movable(abc.ABC):
    """Abstract class for movable objects."""
    
    @abc.abstractmethod
    def move(self, x: float, y: float) -> None:
        """Abstract method for moving."""
        pass


class DrawableMovableShape(Shape, Drawable, Movable):
    """Class inheriting from multiple abstract classes."""
    
    def __init__(self, x: float, y: float) -> None:
        self.x = x
        self.y = y
    
    def area(self) -> float:
        """Must implement Shape.area()."""
        return 0.0
    
    def perimeter(self) -> float:
        """Must implement Shape.perimeter()."""
        return 0.0
    
    def draw(self) -> str:
        """Must implement Drawable.draw()."""
        return f"Drawing at ({self.x}, {self.y})"
    
    def move(self, x: float, y: float) -> None:
        """Must implement Movable.move()."""
        self.x = x
        self.y = y


if __name__ == "__main__":
    print("=== Static Methods ===")
    print(f"MathUtils.add(5, 3): {MathUtils.add(5, 3)}")
    print(f"MathUtils.multiply(4, 7): {MathUtils.multiply(4, 7)}")
    
    print("\n=== Class Methods ===")
    date1 = Date.from_string("2023-12-25")
    print(f"Date from string: {date1}")
    
    print("\n=== Abstract Classes ===")
    rect = Rectangle(5, 3)
    circle = Circle(2)
    print(f"Rectangle: {rect.describe()}")
    print(f"Circle: {circle.describe()}")
    
    print("\n=== Multiple Inheritance ===")
    shape = DrawableMovableShape(10, 20)
    print(shape.draw())
    shape.move(15, 25)
    print(shape.draw())
