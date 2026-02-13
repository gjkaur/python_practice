"""
PCPP 1.9, 1.10: Practice Exercises - Advanced Exceptions & Object Copying
"""

import copy
import traceback


# Exercise 1: Exception Chaining
# TODO: Create a custom exception hierarchy:
#   - BaseException: FileProcessingError
#   - Subclass: FileNotFoundError (custom, not built-in)
#   - Subclass: InvalidFormatError
#   Create a function that reads a file and chains exceptions appropriately

class FileProcessingError(Exception):
    """Base exception for file processing."""
    pass


class FileNotFoundError(FileProcessingError):
    """Custom file not found error."""
    pass


class InvalidFormatError(FileProcessingError):
    """Invalid file format error."""
    pass


# TODO: Implement function with exception chaining
def process_file(filename: str) -> None:
    """Process file with exception chaining."""
    pass


# Exercise 2: Traceback Analysis
# TODO: Create a function that:
#   - Catches an exception
#   - Extracts traceback information
#   - Formats it for logging
#   - Returns structured information

def extract_exception_info(exc: Exception) -> dict:
    """Extract information from exception."""
    # TODO: Implement
    pass


# Exercise 3: Shallow vs Deep Copy
# TODO: Create a class with nested mutable attributes
#   Demonstrate the difference between shallow and deep copy
#   Show when modifying nested objects affects the original

class ComplexObject:
    """Object with nested mutable attributes."""
    # TODO: Implement
    pass


# Exercise 4: Custom Copy Methods
# TODO: Implement __copy__ and __deepcopy__ methods for a class
#   Control how the object is copied

class CustomCopyable:
    """Class with custom copy behavior."""
    # TODO: Implement __copy__ and __deepcopy__
    pass


if __name__ == "__main__":
    print("Complete the exercises above!")
