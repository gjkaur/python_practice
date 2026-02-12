"""Custom exceptions (PCAP 2.2)."""

class ValidationError(Exception):
    pass

class InvalidAmountError(ValidationError):
    pass

class InvalidDateError(ValidationError):
    pass
