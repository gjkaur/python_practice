"""Demonstrate except variants, raise, and custom exception (PCAP 2.1-2.2)."""

class ValidationError(Exception):
    """Custom exception (PCAP 2.2)."""
    pass

# except E as e, e.args (PCAP 2.1)
try:
    int("not a number")
except ValueError as e:
    print("Caught ValueError:", e.args)

# raise and custom exception
try:
    raise ValidationError("Invalid value")
except ValidationError as e:
    print("Caught ValidationError:", e)

# re-raise
try:
    try:
        raise ValueError("inner")
    except ValueError:
        raise  # re-raise
except ValueError as e:
    print("Re-raised:", e.args)
