"""Validators that raise custom exceptions (PCAP 2.1-2.2)."""
from exceptions import RequiredError, FormatError

def validate_non_empty(value: str, field: str = "value") -> str:
    if not value or not value.strip():
        raise RequiredError(f"{field} is required")
    return value.strip()

def validate_int(value: str, field: str = "value") -> int:
    validate_non_empty(value, field)
    try:
        return int(value)
    except ValueError as e:
        raise FormatError(f"{field} must be an integer") from e
