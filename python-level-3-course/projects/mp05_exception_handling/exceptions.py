"""
MP05: Exception Handling System

PCPP Objectives: 1.9, 1.10

Custom exception hierarchy and chaining.
"""


# TODO: Create exception hierarchy
class ProcessingError(Exception):
    """Base exception for processing errors."""
    pass


class FileError(ProcessingError):
    """File-related errors."""
    pass


class ValidationError(ProcessingError):
    """Validation errors."""
    pass


# TODO: Implement functions with exception chaining
def read_file(filename: str) -> str:
    """Read file with exception chaining."""
    # TODO: Implement with implicit chaining
    pass


def process_data(data: str) -> dict:
    """Process data with exception chaining."""
    # TODO: Implement with explicit chaining
    # raise ProcessingError from original exception
    pass
