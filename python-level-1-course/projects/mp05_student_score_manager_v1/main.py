"""
CLI entrypoint for Student Score Manager v1.
"""

from __future__ import annotations

from repository import Scores, add_or_update_student, get_all_students
from stats import compute_average, compute_max, compute_min


def read_int(prompt: str, min_value: int, max_value: int) -> int:
    while True:
        raw = input(prompt)
        try:
            value = int(raw)
        except ValueError:
            print("Please enter a valid integer.")
            continue
        if value < min_value or value > max_value:
            print(f"Value must be between {min_value} and {max_value}.")
            continue
        return value


def print_menu() -> None:
    print("Student Score Manager v1")
    print("------------------------")
    print("1) Add or update student")
    print("2) List students")
    print("3) Show statistics")
    print("0) Exit")


def list_students(scores: Scores) -> None:
    if not scores:
        print("No students recorded yet.")
        return
    for name, score in scores.items():
        print(f"{name}: {score}")


def show_statistics(scores: Scores) -> None:
    if not scores:
        print("No students recorded yet.")
        return
    values = list(scores.values())
    minimum = compute_min(values)
    maximum = compute_max(values)
    average = compute_average(values)
    print(f"Students: {len(values)}")
    print(f"Min score: {minimum}")
    print(f"Max score: {maximum}")
    print(f"Average : {average:.2f}" if average is not None else "Average : N/A")


def main() -> None:
    scores: Scores = {}

    while True:
        print_menu()
        choice = input("Choose: ").strip()

        if choice == "1":
            name = input("Student name: ").strip()
            if not name:
                print("Name cannot be empty.")
                continue
            score = read_int("Score (0-100): ", 0, 100)
            add_or_update_student(scores, name, score)
            print("Saved.")

        elif choice == "2":
            list_students(scores)

        elif choice == "3":
            show_statistics(scores)

        elif choice == "0":
            break

        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()

