"""Validation (PCAP 2.x)."""
from exceptions import ValidationError

def validate_quantity(value: str) -> int:
    try:
        x = int(value)
        if x < 0:
            raise ValidationError("Quantity must be >= 0")
        return x
    except ValueError as e:
        raise ValidationError("Quantity must be an integer") from e
