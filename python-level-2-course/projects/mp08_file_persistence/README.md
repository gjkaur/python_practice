# MP08 – File-Based Persistence Layer

**PCAP**: 5.4–5.5 (I/O, open, read/write, errno)

## Problem

Build a small **persistence layer**: save and load data (e.g. one JSON-like line or simple format) to a file. Use **open()**, **read**/ **write**/ **readlines()**, handle **errno** when file is missing, and optionally use **bytearray** for a buffer.

## User Stories

- As a user I can "save" a string or list of lines and "load" it back.
- As a learner I use text mode, close files (or with), and catch OSError with e.errno.

## Suggested Structure

- `storage.py` – save_text(path, content), load_text(path) returning content or None on error; handle FileNotFoundError/OSError and errno.
- `main.py` – prompt for path and content, save, then load and print.

## Test Cases

1. Save "hello" to a file; load and get "hello".
2. Load from nonexistent file → handle OSError, print or return None.
3. readlines() used for line-by-line load (optional).
