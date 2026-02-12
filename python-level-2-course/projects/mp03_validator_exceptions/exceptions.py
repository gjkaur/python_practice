"""Custom exception hierarchy (PCAP 2.2)."""

class ValidationError(Exception):
    """Base for validation failures."""
    pass

class RequiredError(ValidationError):
    """Required field missing."""
    pass

class FormatError(ValidationError):
    """Invalid format."""
    pass
