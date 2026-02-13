"""
PCPP 1.2: Magic Methods & Special Methods Demo

Demonstrates:
- Comparison methods (__eq__, __lt__, etc.)
- Numeric methods (__add__, __sub__, etc.)
- Type conversion methods (__str__, __repr__, __int__, etc.)
- Attribute access methods (__getattr__, __setattr__)
- Container methods (__getitem__, __len__, __iter__)
"""

from functools import total_ordering
from typing import Any, Iterator


# PCPP 1.2: Comparison Methods
@total_ordering
class Point:
    """Point class demonstrating comparison magic methods."""
    
    def __init__(self, x: float, y: float) -> None:
        """Initialize a Point.
        
        Args:
            x: X coordinate
            y: Y coordinate
        """
        self.x = x
        self.y = y
    
    def __eq__(self, other: object) -> bool:
        """PCPP 1.2: Equality comparison."""
        if not isinstance(other, Point):
            return NotImplemented
        return self.x == other.x and self.y == other.y
    
    def __lt__(self, other: 'Point') -> bool:
        """PCPP 1.2: Less-than comparison (distance from origin).
        
        With @total_ordering, this enables all comparison operators.
        """
        if not isinstance(other, Point):
            return NotImplemented
        return (self.x ** 2 + self.y ** 2) < (other.x ** 2 + other.y ** 2)
    
    def __str__(self) -> str:
        """PCPP 1.2: User-friendly string representation."""
        return f"Point({self.x}, {self.y})"
    
    def __repr__(self) -> str:
        """PCPP 1.2: Developer-friendly representation (should be evaluable)."""
        return f"Point(x={self.x}, y={self.y})"


# PCPP 1.2: Numeric Methods
class Vector:
    """Vector class demonstrating numeric magic methods."""
    
    def __init__(self, x: float, y: float) -> None:
        """Initialize a Vector.
        
        Args:
            x: X component
            y: Y component
        """
        self.x = x
        self.y = y
    
    def __add__(self, other: 'Vector') -> 'Vector':
        """PCPP 1.2: Addition - self + other."""
        if not isinstance(other, Vector):
            return NotImplemented
        return Vector(self.x + other.x, self.y + other.y)
    
    def __radd__(self, other: Any) -> 'Vector':
        """PCPP 1.2: Right-hand addition - other + self."""
        if other == 0:  # Allows sum() to work
            return self
        return NotImplemented
    
    def __mul__(self, scalar: float) -> 'Vector':
        """PCPP 1.2: Scalar multiplication."""
        if not isinstance(scalar, (int, float)):
            return NotImplemented
        return Vector(self.x * scalar, self.y * scalar)
    
    def __rmul__(self, scalar: float) -> 'Vector':
        """PCPP 1.2: Right-hand multiplication - scalar * self."""
        return self.__mul__(scalar)
    
    def __abs__(self) -> float:
        """PCPP 1.2: Absolute value (magnitude)."""
        return (self.x ** 2 + self.y ** 2) ** 0.5
    
    def __str__(self) -> str:
        """String representation."""
        return f"Vector({self.x}, {self.y})"
    
    def __repr__(self) -> str:
        """Developer representation."""
        return f"Vector(x={self.x}, y={self.y})"


# PCPP 1.2: Type Conversion Methods
class Fraction:
    """Fraction class demonstrating type conversion methods."""
    
    def __init__(self, numerator: int, denominator: int = 1) -> None:
        """Initialize a Fraction.
        
        Args:
            numerator: Numerator
            denominator: Denominator (default: 1)
        """
        if denominator == 0:
            raise ValueError("Denominator cannot be zero")
        self.numerator = numerator
        self.denominator = denominator
    
    def __float__(self) -> float:
        """PCPP 1.2: Convert to float."""
        return self.numerator / self.denominator
    
    def __int__(self) -> int:
        """PCPP 1.2: Convert to int (truncates)."""
        return self.numerator // self.denominator
    
    def __str__(self) -> str:
        """PCPP 1.2: User-friendly string."""
        return f"{self.numerator}/{self.denominator}"
    
    def __repr__(self) -> str:
        """PCPP 1.2: Developer representation (evaluable)."""
        return f"Fraction({self.numerator}, {self.denominator})"
    
    def __bool__(self) -> bool:
        """PCPP 1.2: Truthiness (non-zero fraction is truthy)."""
        return self.numerator != 0


# PCPP 1.2: Attribute Access Methods
class Config:
    """Config class demonstrating attribute access methods."""
    
    def __init__(self) -> None:
        """Initialize Config with default values."""
        self._data: dict[str, Any] = {}
        self._defaults = {'host': 'localhost', 'port': 8080}
    
    def __getattr__(self, name: str) -> Any:
        """PCPP 1.2: Called when attribute not found via normal lookup."""
        if name in self._defaults:
            return self._defaults[name]
        raise AttributeError(f"'{type(self).__name__}' object has no attribute '{name}'")
    
    def __setattr__(self, name: str, value: Any) -> None:
        """PCPP 1.2: Called when setting any attribute."""
        if name.startswith('_'):
            # Allow setting private attributes normally
            super().__setattr__(name, value)
        else:
            # Store public attributes in _data dict
            if not hasattr(self, '_data'):
                super().__setattr__('_data', {})
            self._data[name] = value
    
    def __getitem__(self, key: str) -> Any:
        """PCPP 1.2: Allow dict-like access."""
        return self._data.get(key, self._defaults.get(key))


# PCPP 1.2: Container Methods
class Deck:
    """Deck class demonstrating container methods."""
    
    def __init__(self, cards: list[str] | None = None) -> None:
        """Initialize a Deck.
        
        Args:
            cards: List of card names (default: standard 52-card deck)
        """
        if cards is None:
            suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
            ranks = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
            cards = [f"{rank} of {suit}" for suit in suits for rank in ranks]
        self._cards = cards
    
    def __getitem__(self, index: int | slice) -> str | list[str]:
        """PCPP 1.2: Make deck subscriptable like a list."""
        return self._cards[index]
    
    def __len__(self) -> int:
        """PCPP 1.2: Return number of cards."""
        return len(self._cards)
    
    def __contains__(self, card: str) -> bool:
        """PCPP 1.2: Check if card is in deck."""
        return card in self._cards
    
    def __iter__(self) -> Iterator[str]:
        """PCPP 1.2: Make deck iterable."""
        return iter(self._cards)
    
    def __str__(self) -> str:
        """String representation."""
        return f"Deck({len(self)} cards)"


# PCPP 1.2: Introspection Methods
class CustomType:
    """Custom type demonstrating introspection methods."""
    
    def __instancecheck__(self, instance: object) -> bool:
        """PCPP 1.2: Custom isinstance() behavior."""
        # Example: treat strings as instances of this type
        return isinstance(instance, str)
    
    def __subclasscheck__(self, subclass: type) -> bool:
        """PCPP 1.2: Custom issubclass() behavior."""
        # Example: treat str as a subclass
        return issubclass(subclass, str)


if __name__ == "__main__":
    print("=== Comparison Methods ===")
    p1 = Point(1, 2)
    p2 = Point(3, 4)
    p3 = Point(1, 2)
    
    print(f"p1 == p3: {p1 == p3}")
    print(f"p1 < p2: {p1 < p2}")
    print(f"p1 <= p2: {p1 <= p2}")  # Works because of @total_ordering
    
    print("\n=== Numeric Methods ===")
    v1 = Vector(1, 2)
    v2 = Vector(3, 4)
    v3 = v1 + v2
    v4 = v1 * 2
    v5 = 3 * v1  # Right-hand multiplication
    
    print(f"v1 + v2 = {v3}")
    print(f"v1 * 2 = {v4}")
    print(f"3 * v1 = {v5}")
    print(f"|v1| = {abs(v1)}")
    
    print("\n=== Type Conversion ===")
    f = Fraction(3, 4)
    print(f"Fraction: {f}")
    print(f"float(f): {float(f)}")
    print(f"int(f): {int(f)}")
    print(f"bool(f): {bool(f)}")
    print(f"bool(Fraction(0, 1)): {bool(Fraction(0, 1))}")
    
    print("\n=== Attribute Access ===")
    config = Config()
    print(f"config.host: {config.host}")  # Uses __getattr__
    config.port = 9000  # Uses __setattr__
    print(f"config.port: {config.port}")
    print(f"config['host']: {config['host']}")  # Uses __getitem__
    
    print("\n=== Container Methods ===")
    deck = Deck()
    print(f"Deck length: {len(deck)}")
    print(f"First card: {deck[0]}")
    print(f"'Ace of Spades' in deck: {'Ace of Spades' in deck}")
    print(f"First 5 cards: {deck[:5]}")
    
    print("\n=== Iteration ===")
    for i, card in enumerate(deck[:5]):
        print(f"  {i+1}. {card}")
