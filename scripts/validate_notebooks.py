"""Validate all concept notebooks for GitHub/Jupyter compatibility."""
from __future__ import annotations

import json
import sys
from pathlib import Path

import nbformat
from nbformat.validator import normalize, validate

ROOT = Path(__file__).resolve().parents[1]


def main() -> int:
    paths = sorted(ROOT.glob("python-level-*-course/modules/*/*_Concepts.ipynb"))
    errors: list[str] = []
    sizes: list[tuple[int, str]] = []

    for path in paths:
        rel = path.relative_to(ROOT).as_posix()
        sizes.append((path.stat().st_size, rel))
        try:
            with path.open(encoding="utf-8") as f:
                nb = nbformat.read(f, as_version=4)
            normalize(nb)
            validate(nb)
        except Exception as e:
            errors.append(f"{rel}: {type(e).__name__}: {e}")

    print("=== nbformat validation errors ===")
    for err in errors:
        print(err)
    print(f"Total errors: {len(errors)}")

    print("\n=== Largest notebooks ===")
    for size, rel in sorted(sizes, reverse=True)[:12]:
        print(f"{size / 1024:.1f} KB  {rel}")

    # Try nbconvert HTML (what GitHub uses internally)
    print("\n=== nbconvert HTML conversion ===")
    from nbconvert import HTMLExporter

    exporter = HTMLExporter()
    convert_errors: list[str] = []
    for path in paths:
        rel = path.relative_to(ROOT).as_posix()
        try:
            with path.open(encoding="utf-8") as f:
                nb = nbformat.read(f, as_version=4)
            exporter.from_notebook_node(nb)
        except Exception as e:
            convert_errors.append(f"{rel}: {type(e).__name__}: {e}")

    for err in convert_errors:
        print(err)
    print(f"Convert errors: {len(convert_errors)}")

    return 1 if errors or convert_errors else 0


if __name__ == "__main__":
    sys.exit(main())
