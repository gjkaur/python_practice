"""
Example: Defensive input and exception handling.
"""
def read_int_safe(prompt: str) -> int | None:
    """Return int or None on invalid input."""
    raw = input(prompt)
    try:
        return int(raw)
    except ValueError:
        return None

# Prefer validation before operation when possible
def divide(a: float, b: float) -> float:
    if b == 0:
        raise ValueError("b must not be zero")
    return a / b
