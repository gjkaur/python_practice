"""Practice: Exceptions (PCAP 2.1-2.2).

Implement the exception class and functions. Run main() to test.
"""


# --- Task 1: Custom exception (PCAP 2.2) ---
class MyError(Exception):
    """Custom exception for practice."""
    pass


# --- Task 2: Catch and return args (PCAP 2.1) ---
def safe_int(s: str) -> int | None:
    """Convert s to int; on ValueError return None (do not raise)."""
    try:
        return int(s)
    except ValueError:
        return None


# --- Task 3: Raise custom exception (PCAP 2.2) ---
def require_positive(n: int) -> None:
    """If n <= 0, raise MyError with message 'n must be positive'. Otherwise do nothing."""
    if n <= 0:
        raise MyError("n must be positive")


def main() -> None:
    print("safe_int('42'):", safe_int("42"))
    print("safe_int('x'):", safe_int("x"))
    try:
        require_positive(0)
    except MyError as e:
        print("Caught MyError:", e.args)
    require_positive(1)  # no raise


if __name__ == "__main__":
    main()
