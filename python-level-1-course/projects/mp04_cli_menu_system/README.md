## MP04 – CLI Menu System

### 1. Problem Statement

You need a reusable **menu framework** for simple command-line tools.  
The menu should present options, accept user choices, validate input, and dispatch to corresponding actions without turning into spaghetti code.

This will become a pattern you can reuse in many internal tools.

---

### 2. User Stories

- **As a user**, I want a simple, clear menu to interact with a tool.
- **As a developer**, I want menu handling to be centralized and easy to extend.
- **As a maintainer**, I want each menu action implemented in a small, focused function.

---

### 3. Inputs and Outputs

**Inputs**

- User selects options by typing a menu number or command keyword.

Example options:

- `1` – Show help.
- `2` – Show current configuration (hard-coded for now).
- `3` – Run a demo action (e.g., print a random motivational message).
- `0` – Exit.

**Outputs**

- For each choice, the tool prints relevant information or performs a small action.
- Invalid choices produce a friendly error and re-display the menu.

---

### 4. Constraints and Validation Rules

- The menu loop must **never crash** on invalid input; it should recover.
- Menu actions must be implemented as **separate functions**, not inline in the loop.
- Use straightforward control flow; avoid deeply nested `if` blocks.

---

### 5. Suggested Architecture

```text
mp04_cli_menu_system/
  main.py        # menu loop and CLI entrypoint
  actions.py     # functions for each menu option
  validators.py  # input validation helpers
  README.md
```

Responsibilities:

- `validators.py`
  - `read_menu_choice(prompt: str, valid_choices: list[str]) -> str`
- `actions.py`
  - `show_help()`
  - `show_config()`
  - `run_demo()`
- `main.py`
  - Builds and runs the menu loop, calling actions by choice.

---

### 6. CLI Usage Examples

```bash
python main.py
```

Example interaction:

```text
Main Menu
---------
1) Help
2) Show configuration
3) Run demo
0) Exit

Choose an option: 3
Running demo action...

Choose an option: x
Invalid choice. Please try again.
```

---

### 7. Test Cases (At Least 8)

1. **Valid choice – help** → `show_help()` is called; menu returns afterward.
2. **Valid choice – config** → `show_config()` displays static configuration.
3. **Valid choice – demo** → `run_demo()` output observed; no crash.
4. **Exit choice** → selecting `0` ends the loop cleanly.
5. **Invalid choice (string)** → message + re-prompt, no crash.
6. **Invalid choice (out of range number)** → message + re-prompt, no crash.
7. **Multiple actions in sequence** → structure remains correct, no state leakage.
8. **Code inspection test** → ensure no large blocks of business logic live in `main()`; all actions in `actions.py`.

---

### 8. Level-Up Extensions

- Refactor to support **sub-menus** (nested structures).
- Allow both **numbers and commands** (e.g., `1` or `help`).
- Add simple **command logging** to a file.
- Turn the menu into a reusable module that other projects can import.

