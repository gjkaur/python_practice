"""
CLI entrypoint for the Unit Converter mini-project.

Usage:
    python main.py
"""

from __future__ import annotations

from converters import c_to_f, f_to_c, km_to_miles, miles_to_km
from validators import read_float


def print_menu() -> None:
    print("Unit Converter")
    print("--------------")
    print("1) Celsius to Fahrenheit")
    print("2) Fahrenheit to Celsius")
    print("3) Kilometers to Miles")
    print("4) Miles to Kilometers")
    print("0) Exit")


def handle_choice(choice: str) -> bool:
    """
    Handle a single menu choice.

    Returns False if the caller should exit the loop, True otherwise.
    """
    if choice == "1":
        c = read_float("Enter value in Celsius: ")
        result = c_to_f(c)
        print(f"Result: {result:.2f} °F")
    elif choice == "2":
        f = read_float("Enter value in Fahrenheit: ")
        result = f_to_c(f)
        print(f"Result: {result:.2f} °C")
    elif choice == "3":
        km = read_float("Enter distance in kilometers: ")
        result = km_to_miles(km)
        print(f"Result: {result:.2f} miles")
    elif choice == "4":
        miles = read_float("Enter distance in miles: ")
        result = miles_to_km(miles)
        print(f"Result: {result:.2f} km")
    elif choice == "0":
        return False
    else:
        print("Invalid choice. Please try again.")
    return True


def main() -> None:
    while True:
        print_menu()
        choice = input("Choose an option: ").strip()
        if not handle_choice(choice):
            break


if __name__ == "__main__":
    main()

