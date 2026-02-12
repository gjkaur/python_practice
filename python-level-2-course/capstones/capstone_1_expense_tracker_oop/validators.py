"""Input validation; raises custom exceptions (PCAP 2.1-2.2)."""
from exceptions import InvalidAmountError, InvalidDateError

def validate_amount(value: str) -> float:
    try:
        x = float(value)
        if x <= 0:
            raise InvalidAmountError("Amount must be positive")
        return x
    except ValueError as e:
        raise InvalidAmountError("Amount must be a number") from e

def validate_date(value: str) -> str:
    s = value.strip()
    if not s or len(s) < 8:
        raise InvalidDateError("Date too short (use YYYY-MM-DD)")
    return s
