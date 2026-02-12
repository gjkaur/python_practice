"""
CLI entrypoint for the reusable CLI Menu System.
"""

from __future__ import annotations

from actions import run_demo, show_config, show_help
from validators import read_menu_choice


def print_menu() -> None:
    print("Main Menu")
    print("---------")
    print("1) Help")
    print("2) Show configuration")
    print("3) Run demo")
    print("0) Exit")


def handle_choice(choice: str) -> bool:
    """Dispatch based on the user's menu choice."""
    if choice == "1":
        show_help()
    elif choice == "2":
        show_config()
    elif choice == "3":
        run_demo()
    elif choice == "0":
        return False
    else:
        # This path should not occur if validator is used correctly.
        print("Unexpected choice encountered.")
    return True


def main() -> None:
    valid_choices = ["0", "1", "2", "3"]
    while True:
        print_menu()
        choice = read_menu_choice("Choose an option: ", valid_choices)
        if not handle_choice(choice):
            break


if __name__ == "__main__":
    main()

