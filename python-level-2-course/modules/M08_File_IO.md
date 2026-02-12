## M08 – File I/O

**PCAP Alignment**: Section 5 (5.4–5.5) – I/O terminology and operations.  
**Professional Focus**: Safe file handling, context managers (mention), text vs binary.

---

### 1. Outcomes

By the end of this module you will:

- Understand **I/O modes**, **predefined streams**, **handles vs streams**, **text vs binary** modes.
- Use the **open()** function with mode (r, w, a, and b for binary).
- Use **errno** and its values when handling OSError.
- Use **close()**, **.read()**, **.write()**, **.readline()**, **readlines()**.
- Use **bytearray** as an input/output buffer.

---

### 2. Core Concepts (PCAP 5.4–5.5)

#### 2.1 I/O terminology (PCAP 5.4)

- I/O modes: read, write, append; text vs binary (t vs b).
- Predefined streams: stdin, stdout, stderr. Handle: object returned by open(); stream: abstraction for data flow.

#### 2.2 open() and operations (PCAP 5.5)

- open(path, mode="r", encoding="utf-8") for text; open(path, "rb") for binary.
- close() to release; .read(), .readline(), .readlines(); .write().
- errno: attribute on OSError (e.errno); compare to errno module constants (e.g. errno.ENOENT).

#### 2.3 bytearray as buffer

- bytearray() for mutable bytes; write to file in binary mode or read into bytearray.

---

### 3. Exercises (10+)

1. Open a file for reading (text); read() and print first 100 chars.
2. Open for writing; write a few lines; close; reopen and read back.
3. Use readline() in a loop to process a file line by line.
4. Use readlines() and process the list.
5. Open in binary mode "rb"; read bytes; show type and length.
6. Write bytearray to a binary file; read back and compare.
7. Trigger FileNotFoundError; catch OSError and print e.errno; compare to errno.ENOENT.
8. Open in append mode "a"; write a line; verify append.
9. Use open() with encoding="utf-8" and write a string with non-ASCII char; read back.
10. Read a small file into a bytearray buffer (e.g. read(10) into bytearray(10)).

---

### 4. Mini-Project – File-Based Persistence or Log Processor

#### 4.1 Problem Statement

Build a small **file-based persistence** layer or **log processor**: **open**/ **read**/ **write**/ **close** (or **with**); handle **missing file** (e.g. **errno.ENOENT**); use text or binary as appropriate; optional **bytearray** for a small buffer.

#### 4.2 Requirements

- Use **with open(...) as f** for all file I/O; specify **encoding="utf-8"** for text files.
- Implement at least **read** and **write** (e.g. save/load a small config or append log lines).
- Catch **OSError** (or **FileNotFoundError**) when opening a missing file; use **e.errno == errno.ENOENT** or **isinstance(e, FileNotFoundError)** and handle gracefully (e.g. create default or print message).
- Optional: use **bytearray** for a small binary buffer (e.g. read N bytes into buffer).
- **main()** entrypoint; PEP 8 and docstrings.

#### 4.3 Suggested Folder Structure

```text
mp08_file_tool/
  main.py
  file_utils.py   # read_file, write_file, safe_open
  README.md
```

#### 4.4 Acceptance Tests (High-Level)

- Writing then reading back produces the same content; encoding is explicit.
- Opening a nonexistent file is caught and handled (no uncaught FileNotFoundError).
- **with** is used so files are closed; no bare **open()** without close or with.

---

### 5. Code Review Checklist

- [ ] Files closed (or use with statement); OSError handled.
- [ ] Encoding specified for text mode.
- [ ] Binary vs text mode chosen correctly.

---

### 6. Interview-Style Questions

1. What is the difference between text and binary mode?
2. What does open() return? What is a “handle”?
3. When would you use readline() vs read() vs readlines()?
4. What is errno? How do you use it with OSError?
5. Why is it important to close files?
6. What is bytearray? How is it used with I/O?
7. What are the main open() modes (r, w, a, b)?
8. What are predefined streams (stdin, stdout, stderr)?
