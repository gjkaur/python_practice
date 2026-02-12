"""
Menu actions for the CLI Menu System.

Each action is a small, focused function. Logic here should be
easy to reuse in other small CLIs.
"""

from __future__ import annotations


def show_help() -> None:
    """Print a short help message."""
    print("This is a demo CLI menu system.")
    print("Choose an option to see it in action.")


def show_config() -> None:
    """Show a simple, hard-coded configuration."""
    print("Configuration:")
    print("- environment: development")
    print("- feature_flags: []")


def run_demo() -> None:
    """Run a simple demo action."""
    print("Running demo action...")
    print("Imagine some useful work happening here.")

