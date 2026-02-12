"""
CLI entrypoint for the Safe Calculator.
"""

from __future__ import annotations

from io_utils import read_float, read_operation
from operations import add, divide, multiply, subtract


def main() -> None:
    print("Safe Calculator")
    print("---------------")

    while True:
        op = read_operation("Operation (+, -, *, /) or q to quit: ")
        if op == "q":
            break

        a = read_float("First number: ")
        b = read_float("Second number: ")

        try:
            if op == "+":
                result = add(a, b)
            elif op == "-":
                result = subtract(a, b)
            elif op == "*":
                result = multiply(a, b)
            elif op == "/":
                result = divide(a, b)
            else:
                print("Unexpected operation.")
                continue
        except ValueError as exc:
            print(f"Error: {exc}")
        else:
            print(f"Result: {result}")


if __name__ == "__main__":
    main()

