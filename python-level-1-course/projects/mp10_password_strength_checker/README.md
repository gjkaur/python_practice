## MP10 – Password Strength Checker

### 1. Problem Statement

You are implementing a simple **password strength checker** for a CLI tool.  
Given a password string, the tool should:

- Classify it as `WEAK`, `MEDIUM`, or `STRONG` based on defined rules.
- Explain **why** the password received that rating.

This project focuses on string processing, conditionals, and clean validation logic.

---

### 2. User Stories

- **As a user**, I want quick feedback on whether my password is reasonably strong.
- **As a developer**, I want clear, testable rules for password validation.
- **As a security-conscious reviewer**, I want to see transparent criteria (this is a teaching example, not production security).

---

### 3. Inputs and Outputs

**Inputs**

- Password string entered via CLI.

**Outputs**

- Strength classification.
- Reasons explaining the classification.

Example:

```text
Enter password: P@ssw0rd
Strength: MEDIUM
Reasons :
- Length is at least 8 characters.
- Contains upper and lower case letters.
- Contains digits.
- Missing special characters from the required set.
```

---

### 4. Constraints and Validation Rules

Define clear rules such as:

- **WEAK** if:
  - Length < 8, or
  - Only one character type is present.
- **MEDIUM** if:
  - Length >= 8 and at least two character types present.
- **STRONG** if:
  - Length >= 12 and includes:
    - Uppercase, lowercase, digit, and special character.

Character types:

- Lowercase letters.
- Uppercase letters.
- Digits.
- Special characters from a defined set (e.g., `!@#$%^&*`).

---

### 5. Suggested Architecture

```text
mp10_password_strength_checker/
  main.py        # CLI
  rules.py       # strength evaluation logic
  formatting.py  # formatting of reasons/messages
  README.md
```

Responsibilities:

- `rules.py`
  - `evaluate_password(password: str) -> tuple[str, list[str]]`
    - Returns strength label and list of reasons.
- `formatting.py`
  - Helpers to format reasons nicely for display.
- `main.py`
  - Reads password (simple input, no masking at Level 1), calls `evaluate_password`, prints results.

---

### 6. CLI Usage Examples

```bash
python main.py
```

Example interaction:

```text
Enter password: abc
Strength: WEAK
Reasons :
- Too short (minimum length is 8).
- Does not contain uppercase letters.
- Does not contain digits.
- Does not contain special characters.
```

---

### 7. Test Cases (At Least 8)

1. **Very short password** (`"abc"`) → `WEAK`, reasons mention length and missing types.
2. **Long but single-type** (`"abcdefghijk"`) → `WEAK`, missing other types.
3. **Medium criteria** (`"Passw0rd"`) → `MEDIUM`, reasons reflect rules.
4. **Strong criteria** (e.g., `"P@ssw0rdStrong!"`) → `STRONG`.
5. **Boundary length 8** – confirm correct classification at minimum medium length.
6. **Boundary length 12** – confirm possible upgrade to strong when other conditions met.
7. **Special character handling** – ensure at least one from the defined set is required for STRONG.
8. **Repeated runs** – multiple evaluations in a single session behave correctly.

---

### 8. Level-Up Extensions

- Add simple checks against a list of **common weak passwords** (e.g., “password”, “123456”).
- Mask input on the terminal (advanced; may depend on environment support).
- Provide suggestions on how to improve a weak password.
- Integrate into other projects as a reusable `rules.py` module.

