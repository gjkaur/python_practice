"""String normalization (PCAP 3.2-3.3)."""

def normalize_whitespace(s: str) -> str:
    return " ".join(s.split())

def normalize_case(s: str, lower: bool = True) -> str:
    return s.lower() if lower else s.upper()

def codepoint_info(s: str) -> list:
    return [(c, ord(c)) for c in s[:5]]
