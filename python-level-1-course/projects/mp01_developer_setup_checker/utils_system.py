"""
System/environment helper utilities for the Developer Setup Checker.

These functions are small, pure (or side-effect free) where possible,
and easy to unit test.
"""

from __future__ import annotations

import os
import platform
import sys
from pathlib import Path


def get_python_version() -> str:
    """Return the current Python version as a human-readable string."""
    return platform.python_version()


def get_python_executable() -> str:
    """Return the path to the Python executable."""
    return sys.executable


def get_platform_info() -> str:
    """Return a concise string describing the current OS/platform."""
    return platform.platform()


def get_cwd() -> str:
    """Return the current working directory as a string."""
    return str(Path.cwd())


def detect_virtualenv() -> str:
    """
    Best-effort detection of an active virtual environment.

    Returns a human-readable description, e.g.:
    - "Active (.venv)" or
    - "Not detected"
    """
    venv = os.environ.get("VIRTUAL_ENV")
    if venv:
        return f"Active ({Path(venv).name})"

    # Fallback – check if executable path hints at venv usage
    executable_path = Path(sys.executable)
    if ".venv" in executable_path.as_posix():
        return "Active (.venv?)"

    return "Not detected"


def build_report() -> dict[str, str]:
    """
    Build a raw environment report as a dictionary.

    This keeps data and presentation separate.
    """
    report: dict[str, str] = {}

    try:
        report["python_version"] = get_python_version()
    except Exception:
        report["python_version"] = "Unknown"

    try:
        report["python_executable"] = get_python_executable()
    except Exception:
        report["python_executable"] = "Unknown"

    try:
        report["platform"] = get_platform_info()
    except Exception:
        report["platform"] = "Unknown"

    try:
        report["cwd"] = get_cwd()
    except Exception:
        report["cwd"] = "Unknown"

    try:
        report["virtualenv"] = detect_virtualenv()
    except Exception:
        report["virtualenv"] = "Unknown"

    return report

