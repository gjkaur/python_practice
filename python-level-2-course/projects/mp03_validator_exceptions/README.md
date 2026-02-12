# MP03 – Validator Library with Custom Exception Hierarchy

**PCAP**: 2.1–2.2 (exceptions, custom exception classes)

## Problem

Build a small **validator** library that raises a **custom exception hierarchy** (e.g. ValidationError, RequiredError, FormatError). Use except variants, raise, and exception args.

## User Stories

- As a caller I get clear exception types and messages when validation fails.
- As a learner I see defining and using self-defined exceptions.

## Suggested Structure

- `exceptions.py` – base ValidationError, subclasses (RequiredError, FormatError).
- `validators.py` – functions that validate and raise these exceptions.
- `main.py` – CLI that validates input and catches/prints exceptions.

## Test Cases

1. Valid input → no exception.
2. Missing required field → RequiredError with message.
3. Bad format → FormatError; catch and print e.args.
4. Re-raise after logging (optional).
