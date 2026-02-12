## MP01 – Developer Setup Checker

### 1. Problem Statement

You are onboarding a new developer to a Python project.  
You need a small CLI tool that verifies their **local environment** is correctly set up and prints a concise report.

The tool should help answer:

- Which Python version is active?
- Is a virtual environment active?
- What is the current working directory?
- Which OS/platform is the script running on?

This mirrors real onboarding scripts and internal “doctor” tools used in professional teams.

---

### 2. User Stories

- **As a new developer**, I want to quickly see whether my environment matches the team’s expectations.
- **As a tech lead**, I want a repeatable way to collect environment information from team members when debugging issues.
- **As a support engineer**, I want a simple report I can ask colleagues to run and paste into chat/tickets.

---

### 3. Inputs and Outputs

**Inputs**

- No command-line arguments required at Level 1.
- Optional: prompt user to confirm whether they expect a virtualenv to be active (yes/no).

**Outputs**

- A structured, human-readable report printed to stdout, including:
  - Python version (e.g., `3.11.2`).
  - Interpreter path.
  - Current working directory.
  - OS/platform.
  - Whether a virtualenv appears to be active.

Example (approximate):

```text
=== Developer Setup Report ===
Python version  : 3.11.2
Python executable: C:\Users\...\python.exe
OS / Platform   : Windows-10-10.0.26200-SP0
CWD             : C:\Users\...\project
Virtualenv      : Active (.venv)  # or "Not detected"
===============================
```

---

### 4. Constraints and Validation Rules

- The script **must not crash** if any individual check fails; it should report “Unknown” and continue.
- Output should be **consistent and PEP 8–friendly** in the code:
  - Use clear function and variable names.
- No external libraries beyond the standard library (`sys`, `platform`, `os`, `pathlib`).

---

### 5. Suggested Architecture

Modules and responsibilities:

- `env_report.py`
  - `main()` – orchestrates checks and printing.
- `utils_system.py`
  - `get_python_version()`
  - `get_python_executable()`
  - `get_platform_info()`
  - `get_cwd()`
  - `detect_virtualenv()`

Design notes:

- Each helper returns **data**, not formatted strings, to keep formatting centralized.
- `main()` should be short and easy to read.

---

### 6. CLI Usage Examples

From repository root (after activating virtualenv if used):

```bash
python env_report.py
```

Expected behavior:

- Prints report.
- Exits with code `0`.

If something goes wrong (e.g., cannot determine platform), the script:

- Prints `Unknown` for that field.
- Still exits cleanly.

---

### 7. Test Cases (At Least 8)

1. **Basic run**:  
   - Precondition: Python installed.  
   - Run `python env_report.py`.  
   - Expect: all sections present, no traceback.
2. **Virtualenv active**:  
   - Activate `.venv`.  
   - Run script.  
   - Expect: “Virtualenv: Active” and interpreter path inside `.venv`.
3. **Virtualenv not active**:  
   - Deactivate any venv.  
   - Run script.  
   - Expect: “Virtualenv: Not detected”.
4. **Different OS** (if possible):  
   - Run on Linux/macOS.  
   - Expect: OS/platform reflects the correct system.
5. **Working directory check**:  
   - Run from subdirectory.  
   - Expect: CWD in report matches that directory.
6. **Function-level tests**:  
   - Import `utils_system` in a REPL and call each helper.  
   - Expect: each returns a non-empty string or a sensible default.
7. **Formatting stability**:  
   - Ensure changes to helpers do not break the layout of the final report.
8. **Error tolerance** (simulated):  
   - Temporarily modify a helper to raise an exception; ensure `main()` catches it and prints “Unknown” for that section (optional stretch).

---

### 8. Level-Up Extensions

- Add optional **command-line flags**:
  - `--json` to emit the report as JSON instead of text.
  - `--short` to skip less-important fields.
- Integrate basic **logging** to a file in addition to console output.
- Add a simple **self-check** that warns if Python version is outside an expected range.

