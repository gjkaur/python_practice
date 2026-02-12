"""
CLI entrypoint for the Developer Setup Checker mini-project.

Usage:
    python env_report.py
"""

from __future__ import annotations

from utils_system import build_report


def format_report(report: dict[str, str]) -> str:
    """Return a human-friendly multi-line string for the environment report."""
    lines = [
        "=== Developer Setup Report ===",
        f"Python version   : {report.get('python_version', 'Unknown')}",
        f"Python executable: {report.get('python_executable', 'Unknown')}",
        f"OS / Platform    : {report.get('platform', 'Unknown')}",
        f"CWD              : {report.get('cwd', 'Unknown')}",
        f"Virtualenv       : {report.get('virtualenv', 'Unknown')}",
        "===============================",
    ]
    return "\n".join(lines)


def main() -> None:
    report = build_report()
    output = format_report(report)
    print(output)


if __name__ == "__main__":
    main()


