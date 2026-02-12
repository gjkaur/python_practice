# MP02 – Small Package with Subpackages

**PCAP**: 1.5 (user-defined modules and packages, __init__.py, __name__)

## Problem

Create a small **package** with at least one **subpackage**, a clear public API via `__init__.py`, and use of `__name__` for script vs import.

## User Stories

- As a user I can `from mp02_small_package import something` and use it.
- As a learner I see nested packages and __init__.py re-exports.

## Suggested Structure

- `mp02_small_package/` (or `pkg/`)
  - `__init__.py` – defines __all__ and/or re-exports from submodules.
  - `utils/` (subpackage)
    - `__init__.py`
    - `helpers.py` – one or two functions.
- `main.py` or `run.py` at project root – imports from package and runs a demo.

## Test Cases

1. `from pkg import foo` works when foo is re-exported in __init__.py.
2. Running a module with `if __name__ == "__main__":` runs demo; importing does not run it.
3. dir(pkg) shows public names.
