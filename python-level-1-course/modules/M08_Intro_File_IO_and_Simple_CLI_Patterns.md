## M08 – Intro File I/O and Simple CLI Patterns

**PCEP Alignment**: Uses fundamentals from Sections 1–4 to build small systems; file I/O itself is an extension beyond PCEP but kept lightweight.  
**Professional Focus**: Reading/writing simple files, structured CLI entrypoints, and basic configuration.

---

### 1. Outcomes (Job-Skill Phrasing)

By the end of this module, a learner should be able to:

- Implement small **CLI tools** with a clear `main()` entrypoint and menu or command patterns.
- Use Python’s built-in `open()` to perform **basic file I/O** (text mode).
- Persist small datasets to **JSON or CSV** files and reload them safely.
- Add a minimal **configuration mechanism** (e.g., settings stored in a JSON file).
- Wire together previously learned skills (data types, control flow, collections, functions, exceptions).

---

### 2. Concept Explanations and Code Examples

#### 2.1 File I/O Basics

```python
def read_text_file(path: str) -> str:
    with open(path, "r", encoding="utf-8") as f:
        return f.read()

def write_text_file(path: str, content: str) -> None:
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
```

Explain:

- Use `with` to ensure files are closed.
- Work in **text mode** (`"r"`, `"w"`) for Level 1.

#### 2.2 JSON for Simple Persistence

```python
import json

def load_json(path: str) -> dict:
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)

def save_json(path: str, data: dict) -> None:
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)
```

Use try/except in calling code to handle I/O failures.

#### 2.3 CLI Entrypoint Pattern

```python
def main() -> None:
    # parse simple commands (no argparse yet)
    while True:
        command = input("Enter command (add/list/quit): ").strip().lower()
        if command == "add":
            handle_add()
        elif command == "list":
            handle_list()
        elif command == "quit":
            break
        else:
            print("Unknown command.")


if __name__ == "__main__":
    main()
```

---

### 3. Edge Cases and Common Mistakes

- Not handling missing files or malformed JSON.
- Ignoring encoding issues (stick to UTF-8).
- Mixing business logic directly into file I/O functions.
- Forgetting to flush or close files (avoided by using `with`).

---

### 4. Production Notes

- Keep file I/O confined to a **storage layer** (e.g., `storage.py`) separate from CLI and business logic.
- Validate data read from files before trusting it.
- For configs, keep **defaults** in code and override with file values where present.

---

### 5. Practice Set (10–15 Exercises)

1. Write a function to read a text file and print the number of lines.
2. Create a script that logs user commands to a file named `commands.log`.
3. Implement `load_json` and `save_json` as shown, then test with a small dictionary.
4. Add basic error handling for when a JSON file is missing or invalid.
5. Design a CLI loop that supports commands `add`, `remove`, `list`, and `quit`.
6. Store a small inventory dict to disk as JSON and load it back.
7. Implement a configuration file with a few settings (e.g., default currency, language).
8. Refactor file I/O out of a previous mini-project into a `storage.py` module.
9. Add a simple “export report” command that writes text output to a file.
10. Ensure that your CLI still behaves sensibly when the data file is empty or missing.

---

### 6. Mini-Project – Configurable Reminder CLI

**Goal**: Build a CLI that reads basic configuration from a file and simulates reminders (no scheduling, just logic).

#### 6.1 Problem Statement

The program should:

- Read a configuration file (JSON) with:
  - Default reminder message.
  - Default number of repetitions.
- Provide commands to:
  - Show the current configuration.
  - Run a reminder loop using the config values.

#### 6.2 Requirements

- Use **JSON** for configuration.
- Separate modules for CLI (`main.py`), config handling (`config.py`), and core logic (`reminders.py`).
- Handle file-not-found or invalid JSON gracefully with defaults and warnings.

#### 6.3 Suggested Folder Structure

```text
mp09_configurable_reminder_cli/
  main.py        # CLI entrypoint
  config.py      # load/save configuration
  reminders.py   # core reminder logic
  config.json    # example configuration
  README.md
```

#### 6.4 Acceptance Tests (High-Level)

- If `config.json` is missing, the app uses safe defaults and informs the user.
- Changing values in `config.json` affects behavior without code changes.
- The CLI does not crash when configuration values are of the wrong type; it reports issues.

---

### 7. Code Review Checklist

- **Structure**
  - [ ] File I/O is encapsulated in dedicated functions/modules.
  - [ ] CLI loop is separated from storage and business logic.
- **Robustness**
  - [ ] File-related errors are handled with clear messages.
  - [ ] Data read from files is validated or used defensively.
- **Extensibility**
  - [ ] Config handling is simple but structured enough to grow in Level 2 (e.g., command-line args, more settings).

---

### 8. Interview-Style Questions

1. How do you open and read a text file safely in Python?
2. What is the advantage of using a `with` block for file I/O?
3. How would you design a simple config system for a CLI app?
4. Where in your architecture should file I/O live, and why?
5. What could go wrong when reading JSON from disk, and how would you handle it?
6. How would you design the entrypoint for a CLI that supports multiple commands?
7. What are the trade-offs between JSON and CSV for storing small datasets?
8. How does this module prepare you for building more complex tools (e.g., log analyzers, inventory systems)?

