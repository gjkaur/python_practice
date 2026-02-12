# MP04 – String/Encoding Normalizer

**PCAP**: 3.1–3.3 (strings, encoding, ord/chr, methods)

## Problem

Build a small **text normalizer** that uses encoding awareness, `ord()`/`chr()`, and string methods (split, join, find, isxxx, etc.). Optionally normalize Unicode or strip/upper/lower.

## User Stories

- As a user I pass a string (or read from stdin) and get normalized output.
- As a learner I use .split(), .join(), .strip(), .lower(), .find(), and optionally encoding.

## Suggested Structure

- `normalizer.py` – functions: normalize_whitespace, normalize_case, maybe codepoint_info(s).
- `main.py` – read line, call normalizer, print.

## Test Cases

1. "  a  b  c  " → "a b c" (single spaces).
2. "HELLO" → "hello" (or configurable).
3. For a given char, print ord and chr (optional).
4. Use .find() to locate a substring and print index.
