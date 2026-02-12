"""Practice: User-defined modules and packages (PCAP 1.5).

1. Define greet(name) that returns 'Hello, {name}!'
2. Add if __name__ == '__main__': and call greet('World')
3. In another script (or REPL) you can: from practice_02_packages import greet; print(greet('Learner'))
"""


def greet(name: str) -> str:
    """Return a greeting string."""
    return f"Hello, {name}!"


def main() -> None:
    print(greet("World"))
    print("__name__ when run as script:", __name__)


if __name__ == "__main__":
    main()
