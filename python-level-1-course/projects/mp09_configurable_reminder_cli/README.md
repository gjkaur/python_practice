## MP09 – Configurable Reminder CLI

### 1. Problem Statement

You are creating a small CLI that simulates “reminders” using configuration loaded from a file.  
The program should:

- Read a JSON config file (e.g., `config.json`) containing:
  - Default reminder message.
  - Default number of repetitions.
- Use that configuration to drive behavior, with safe fallbacks if the file is missing or invalid.

This project introduces basic configuration and file I/O patterns.

---

### 2. User Stories

- **As a user**, I want to change reminder behavior by editing a config file, not the code.
- **As a developer**, I want a clear separation between config loading and reminder logic.
- **As a maintainer**, I want graceful behavior when the config file is misconfigured.

---

### 3. Inputs and Outputs

**Inputs**

- No CLI arguments required in Level 1; config is read from `config.json`.
- Optionally, user can override:
  - Reminder message.
  - Number of repetitions.

**Outputs**

- Reminder lines printed according to configuration, for example:

```text
Reminder: Drink water!
Reminder: Drink water!
Reminder: Drink water!
```

If config is missing:

```text
Warning: config.json not found, using defaults.
```

---

### 4. Constraints and Validation Rules

- Config file should be valid JSON:
  - `{ "message": "Drink water!", "repeat": 3 }`
- If keys are missing or invalid types:
  - Use default values and emit a warning.
- No crashes due to missing or malformed configuration.

---

### 5. Suggested Architecture

```text
mp09_configurable_reminder_cli/
  main.py        # CLI entrypoint
  config.py      # load/save configuration
  reminders.py   # core reminder logic
  config.json    # sample configuration file
  README.md
```

Responsibilities:

- `config.py`
  - `load_config(path: str) -> dict` (returns defaults on failure).
  - Optionally `save_config(path: str, config: dict) -> None`.
- `reminders.py`
  - `run_reminders(message: str, repeat: int) -> None`.
- `main.py`
  - Loads config, optionally allows overrides via input, calls `run_reminders`.

---

### 6. CLI Usage Examples

```bash
python main.py
```

Sample `config.json`:

```json
{
  "message": "Time to stretch!",
  "repeat": 2
}
```

Example output:

```text
Using config from config.json
Reminder: Time to stretch!
Reminder: Time to stretch!
```

---

### 7. Test Cases (At Least 8)

1. **Valid config** – correct message and repeat count used.
2. **Missing config** – defaults used; warning printed.
3. **Malformed JSON** – defaults used; warning printed.
4. **Missing keys** – defaults used for missing values; others read from file.
5. **Invalid types** – e.g., `"repeat": "three"`; fallback to default repeat.
6. **Zero or negative repeat** – treat as zero or fall back to 1 (define behavior).
7. **User override** – if implemented, manual override takes precedence over config.
8. **Idempotence** – running multiple times does not corrupt config.

---

### 8. Level-Up Extensions

- Add command-line arguments to specify an alternative config path.
- Implement saving last-used configuration back to file.
- Add timestamps to reminders or log them to a file.
- Extend config with more options (e.g., categories, different reminder types).

