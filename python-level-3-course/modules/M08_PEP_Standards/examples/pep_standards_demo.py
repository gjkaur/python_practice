"""
PCPP 2.1, 2.2, 2.3: PEP Standards & Best Practices Demo

This module demonstrates PEP 8, PEP 257, and PEP 484 compliance.
"""

from typing import Optional, List, Dict, Any


# PEP 20: The Zen of Python
# Run: import this


# PEP 8: Code Layout and Style
class ExampleClass:
    """Example class demonstrating PEP 8 compliance.
    
    This class follows PEP 8 guidelines for:
    - Naming (PascalCase for classes)
    - Line length (max 79/99 characters)
    - Spacing around operators
    - Docstrings (PEP 257)
    """
    
    # Class variable
    CLASS_CONSTANT: int = 100
    
    def __init__(self, name: str, value: int) -> None:
        """Initialize ExampleClass.
        
        Args:
            name: Name of the instance
            value: Numeric value
        """
        self.name = name
        self.value = value
    
    def calculate(self, multiplier: float) -> float:
        """Calculate value multiplied by multiplier.
        
        Args:
            multiplier: Multiplication factor
            
        Returns:
            Calculated result
        """
        return self.value * multiplier


# PEP 257: Docstrings
def process_data(
    items: List[str],
    filter_func: Optional[callable] = None
) -> Dict[str, int]:
    """Process a list of items and return statistics.
    
    This function demonstrates:
    - Multi-line docstring format
    - Parameter descriptions
    - Return value description
    
    Args:
        items: List of strings to process
        filter_func: Optional function to filter items
        
    Returns:
        Dictionary with statistics (count, filtered_count)
        
    Raises:
        ValueError: If items list is empty
    """
    if not items:
        raise ValueError("Items list cannot be empty")
    
    if filter_func:
        filtered = [item for item in items if filter_func(item)]
    else:
        filtered = items
    
    return {
        'total': len(items),
        'filtered': len(filtered)
    }


# PEP 484: Type Hints
def add_numbers(a: int, b: int) -> int:
    """Add two numbers.
    
    Args:
        a: First number
        b: Second number
        
    Returns:
        Sum of a and b
    """
    return a + b


def process_user_data(
    user_id: str,
    data: Dict[str, Any],
    validate: bool = True
) -> Optional[Dict[str, Any]]:
    """Process user data with optional validation.
    
    Args:
        user_id: Unique user identifier
        data: User data dictionary
        validate: Whether to validate data
        
    Returns:
        Processed data dictionary or None if validation fails
    """
    if validate and not data:
        return None
    return {'id': user_id, **data}


if __name__ == "__main__":
    # PEP 8: Proper spacing and formatting
    obj = ExampleClass("test", 42)
    result = obj.calculate(2.5)
    print(f"Result: {result}")
    
    # Demonstrate type hints
    total = add_numbers(5, 3)
    print(f"Sum: {total}")
    
    # Demonstrate docstrings
    stats = process_data(["a", "b", "c"], lambda x: x != "b")
    print(f"Stats: {stats}")
