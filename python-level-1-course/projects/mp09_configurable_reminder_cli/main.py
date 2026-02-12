"""
CLI entrypoint for the Configurable Reminder mini-project.
"""

from __future__ import annotations

from config import load_config
from reminders import run_reminders


def main() -> None:
    config = load_config("config.json")
    print("Using config:", config)

    message = config["message"]
    repeat = config["repeat"]

    override = input("Override message? (leave blank to keep): ").strip()
    if override:
        message = override

    run_reminders(message=message, repeat=repeat)


if __name__ == "__main__":
    main()

