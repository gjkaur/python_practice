# Week 9 – Strings, File I/O, and CLI Patterns

**Module**: M05 (deeper), M08  
**Mini Project**: [mp09 Configurable Reminder CLI](../projects/mp09_configurable_reminder_cli/)

---

## Learning focus

- PEP 8 and code smells; using `logging` instead of print for operational messages.
- Reading/writing files; JSON config; structured CLI entry points.
- Basic testing of business logic (e.g. assertions or unittest).

---

## Reading and notebooks

- [M05 – Strings](../modules/M05_Strings_and_Text_Processing.md), [M08 – File I/O and CLI](../modules/M08_Intro_File_IO_and_Simple_CLI_Patterns.md)
- [M05](../modules/M05_Strings_and_Text_Processing/M05_Concepts.ipynb) and [M08](../modules/M08_Intro_File_IO_and_Simple_CLI_Patterns/M08_Concepts.ipynb) notebooks
- Run M08 `examples/` and `practice/practice_08_*.py`.

---

## Concepts and practice

1. Read a small text file line by line and print each line with a line number; handle missing file with a clear message.
2. Load a JSON object from a file (e.g. `{"key": "value"}`); print one field; handle missing/invalid file.
3. From the module: complete at least 5 exercises from M08 (and M05 if needed).

---

## Mini project tasks

1. Read [mp09 README](../projects/mp09_configurable_reminder_cli/README.md).
2. Implement Configurable Reminder CLI: load config from `config.json` (message, repeat); run reminders with that config; fallback to defaults if file missing or invalid.
3. Use at least two modules (e.g. config loader, reminder logic); use logging for warnings.
4. Run with config present, missing, and malformed; document behavior.
5. Optionally add a simple test that calls the reminder function with fixed (message, repeat) and checks output or side effect.

---

## Optional

- Add optional CLI args to override message and repeat.
- Add a `save_config` to write defaults to a new file.

---

## Checklist

- [ ] config.json loaded; defaults on failure
- [ ] Reminder output matches config
- [ ] No crash on missing/malformed config
- [ ] Logging or clear warnings used
