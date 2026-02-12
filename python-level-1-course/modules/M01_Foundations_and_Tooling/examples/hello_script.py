"""
Example: Minimal script with main() and __main__ guard.
Run from command line: python hello_script.py
"""
# Concept: script structure, comments, PEP 8 naming


def main() -> None:
    print("Hello, developer!")
    print("This script demonstrates a clear entrypoint.")


if __name__ == "__main__":
    main()
