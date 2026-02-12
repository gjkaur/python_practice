## Level 1 – Mini Project and Capstone Specifications

This document defines detailed specifications for all mini projects (MP1–MP9) and the primary capstones, aligned with the Level 1 roadmap and PCEP-30-02.

Each project includes:
- **Goal**: What the student should learn.
- **Requirements**: Scope and must-have behaviors.
- **Acceptance Criteria**: What “done” looks like.
- **Suggested Extensions**: Optional challenges for fast learners.

---

### MP1 – Developer Setup Checker (Week 1)

**Goal**: Confirm environment setup and practice basic I/O and Git.

**Requirements**
- A Python script that:
  - Prints:
    - Python version.
    - Platform / OS name.
    - Whether a virtual environment (e.g., `.venv/`) exists in the project folder.
  - Uses clear, labeled, and nicely formatted output.
- The project must be in a Git repository:
  - At least one commit that adds this script.
  - `.venv/` (or equivalent) ignored using `.gitignore`.

**Acceptance Criteria**
- Running the script from the project root prints:
  - “Python version: …”
  - “Platform: …”
  - “Virtual environment found: True/False” (or equivalent informative wording).
- Script runs without errors on Windows/macOS/Linux.
- Script follows basic PEP 8 conventions for names and layout.

**Suggested Extensions**
- Check for presence and version of specific packages (e.g., `pip list` or importing a library).
- Exit with status code:
  - `0` if all checks pass.
  - Non-zero if any critical check fails.

---

### MP2 – Unit Converter CLI (Week 2)

**Goal**: Practice numeric operators, I/O, and initial function decomposition.

**Requirements**
- Command-line interface that:
  - Shows a menu of conversion types (at least):
    - Temperature: Celsius ↔ Fahrenheit.
    - Distance: kilometers ↔ miles.
  - Asks the user for:
    - Conversion direction.
    - Numeric value to convert.
  - Validates input and prints clear error messages on invalid input.
- Conversion logic:
  - Implement core conversion formulas in separate functions (e.g., `c_to_f`, `f_to_c`, `km_to_miles`, `miles_to_km`).
  - The CLI must call these functions instead of duplicating formulas.

**Acceptance Criteria**
- All required conversions work correctly within expected precision.
- Invalid input (e.g., “abc”) does not crash the program; instead, the user sees a friendly error and can try again.
- Conversion logic is not duplicated; all uses go through shared functions.
- Names and formatting follow basic PEP 8.

**Suggested Extensions**
- Add additional conversions (e.g., kg ↔ lb, cm ↔ inches).
- Allow the user to perform multiple conversions until they choose to exit.
- Add a simple summary of how many conversions were performed in the session.

---

### MP3 – Admission Eligibility Checker (Week 3)

**Goal**: Implement complex conditional logic and explain decisions clearly.

**Requirements**
- Program that:
  - Prompts the user for several attributes (suggested):
    - Age.
    - Test score.
    - Income bracket or fee category.
    - Flags like “special scholarship candidate”, “returning student”, etc.
  - Encodes multi-criteria decision rules, such as:
    - Eligible if test score ≥ threshold AND age within a given range.
    - Override or special paths for specific flags (e.g., scholarship candidate).
  - Outputs:
    - Final decision: “Eligible” or “Not eligible”.
    - Human-readable explanation of why (e.g., “Eligible: score high enough and within age bracket”).

**Acceptance Criteria**
- The program uses at least:
  - Multiple conditions combined with `and`/`or` operators.
  - Comparison operators (e.g., `>=`, `<=`).
  - At least one nested `if` or clear equivalent structure.
- The logic is expressed with readable intermediate variables, not a single unreadable line.
- No crashes for normal user input; invalid entries are handled or explained.

**Suggested Extensions**
- Support different programs (e.g., “standard track”, “honors track”) each with different rules.
- Log each decision (input and result) to a text file for auditing.

---

### MP4 – CLI Menu System (Week 4)

**Goal**: Practice `while` loops, menus, and user-driven flows.

**Requirements**
- Interactive CLI with at least:
  - A main menu printed to the user with numbered options (minimum 4).
  - A `while` loop that:
    - Repeats the menu.
    - Accepts user selection.
    - Dispatches to appropriate function for each option.
    - Allows the user to exit cleanly.
- Robust handling of invalid input:
  - Wrong menu choice.
  - Non-numeric input when a number is expected.

**Acceptance Criteria**
- Menu redisplays after each action until user chooses “Exit”.
- No unhandled exceptions from simple user mistakes.
- Logic is split into helpers such as `show_menu()`, `handle_choice(choice)`, etc., instead of one huge function.

**Suggested Extensions**
- Add a submenu (e.g., “Settings”) with its own options.
- Maintain state across options (e.g., a collection of items that can be added/removed).

---

### MP5 – Student Score Manager v1 (Week 5)

**Goal**: Use lists and basic aggregation to manage scores.

**Requirements**
- Program that:
  - Stores multiple students and their scores.
  - Supports at least:
    - Add a student with score.
    - List all students with scores.
    - Compute and display minimum, maximum, and average scores.
  - Uses:
    - Either a list of tuples `(name, score)` or parallel lists.
  - Presents a menu-driven CLI (can reuse MP4 patterns).

**Acceptance Criteria**
- Aggregations (min, max, average) are correct.
- The program handles the case of no students gracefully (e.g., prints a message instead of crashing).
- Code uses list operations and iteration, not ad-hoc global variables.

**Suggested Extensions**
- Sort students by name or score before displaying.
- Allow updating or removing a student.
- Add simple grading categories (A/B/C/D/F) based on score.

---

### MP6 – Address Book CLI (Week 6)

**Goal**: Practice dictionaries and basic CRUD with search.

**Requirements**
- CLI address book that:
  - Stores contacts in an in-memory dictionary keyed by unique identifier (name or email).
  - Supports:
    - Add a contact.
    - View all contacts.
    - Search contacts by name or email (substring search acceptable).
    - Delete a contact.
  - Utilizes a menu loop (can build on MP4 structure).

**Acceptance Criteria**
- Deleting or searching for a non-existent contact does not crash.
- Code uses dictionary operations (e.g., `in`, `.get`, `del`) appropriately.
- Basic separation of I/O and logic functions (e.g., `add_contact(contacts, ...)`, `search_contacts(contacts, query)`).

**Suggested Extensions**
- Persist data between runs using JSON or a simple text format.
- Store multiple phone numbers or notes per contact.
- Implement partial matches and case-insensitive search.

---

### MP7 – Functional Refactor (Week 7)

**Goal**: Improve an existing mini project by refactoring into clean functions.

**Requirements**
- Select a previous project (recommended: MP2 or MP6).
- Perform a refactor that:
  - Extracts repeated logic into helper functions.
  - Introduces at least one pure function (no I/O, deterministic output).
  - Cleans up naming and layout using PEP 8.
- Document refactor goals in comments or a short `REFactor_NOTES.md` (optional but recommended).

**Acceptance Criteria**
- Reduced duplication; logic not copy-pasted across the codebase.
- Main script has a clear, small `main()` function orchestrating the flow.
- Core functions have clear parameters and return values instead of using global variables.

**Suggested Extensions**
- Add basic automated tests (or asserts) for new pure functions.
- Introduce a tiny module structure (e.g., split into `cli.py` and `logic.py`).

---

### MP8 – Safe Calculator (Week 8)

**Goal**: Apply exception handling and defensive programming patterns.

**Requirements**
- CLI calculator that:
  - Supports at least the four basic operations: addition, subtraction, multiplication, division.
  - Allows user to enter numbers and operator(s) via prompts or simple expression input.
  - Handles:
    - Non-numeric input using `try/except` around conversions (`ValueError`).
    - Division by zero gracefully (`ZeroDivisionError`).
  - Uses specific exceptions, not bare `except`.

**Acceptance Criteria**
- Program never terminates with an unhandled exception for normal usage.
- Error messages are clear and informative (e.g., “Cannot divide by zero”).
- The validation and calculation steps are reasonably separated into functions.

**Suggested Extensions**
- Support chained calculations or expressions with parentheses, carefully controlling risk (no `eval` for this level).
- Add logging of errors and operations to a log file using the `logging` module.
- Add history feature to review past operations in the session.

---

### MP9 – Configurable Reminder CLI (Week 9)

**Goal**: Combine configuration files, logging, and structured code.

**Requirements**
- CLI tool that:
  - Reads configuration from a JSON or INI file specifying at least:
    - Reminder messages.
    - Number of reminders or interval between reminders (simplified for demo).
  - Uses a loop to print reminders based on configuration.
  - Sets up and uses `logging` to:
    - Log start/stop events.
    - Log each reminder event (and errors if they occur).

**Acceptance Criteria**
- Program fails gracefully when the config file is missing or invalid:
  - Prints or logs a clear error instead of a traceback.
- No hard-coded duplicates of config values in the main code.
- Uses logging with at least INFO and ERROR levels.

**Suggested Extensions**
- Support multiple categories of reminders (e.g., work, break, health) with different frequencies.
- Allow an optional command-line argument specifying the config path.
- Track how many reminders have been sent in a run and print a summary on exit.

---

### Capstone A – CLI Expense Tracker (Week 10)

**Goal**: Build a realistic, data-centric CLI app with modular design.

**Required Folder Structure**
- `expense_tracker/`
  - `__init__.py` (can be empty or hold version).
  - `main.py` – CLI entry point.
  - `models.py` – data structures (e.g., `Expense` representation).
  - `storage.py` – file read/write (CSV or JSON) for expenses.
  - `services.py` – core business logic (add/list/summarize).
  - `config.py` – configuration loading (paths, currency symbol, default categories).
  - `tests/` – basic test files (e.g., `test_services.py`).

**Functional Requirements**
- Core features:
  - Add expense (amount, category, date, optional note).
  - List all expenses, optionally filtered:
    - By category.
    - By date range (optional extension).
  - Summarize expenses:
    - Total spent overall.
    - Total per category.
- Persistence:
  - All expenses written to and read from a data file via `storage.py`.
  - File format: CSV or JSON (pick one, but structure and keys must be documented).
- Input Validation:
  - Amount must be a positive number.
  - Category must be a non-empty string; optional alignment with configured categories.
  - Date must be valid (could be simple “YYYY-MM-DD” string with basic checks).

**Non-Functional Requirements**
- Clear separation of concerns:
  - No direct `input`/`print` in `services.py` or `storage.py`.
  - No direct file I/O in `main.py` (delegated to `storage.py`).
- Logging:
  - Use `logging` to record:
    - When an expense is added.
    - Errors during file operations or parsing.
- Tests:
  - At least 2–3 automated tests for key `services.py` functions (e.g., adding an expense, summarizing by category).
- Documentation:
  - `README` or section in course docs explaining:
    - How to run the tracker.
    - The data format and where the data file is stored.

**Acceptance Criteria**
- All core flows (add/list/summarize) function correctly in normal scenarios.
- Program handles basic error cases (invalid amount, missing file, malformed record) gracefully.
- Module boundaries are respected as described above.
- Tests pass, and testable logic is not entangled with I/O.

**Suggested Extensions**
- Support editing and deleting existing expenses.
- Provide reports:
  - Monthly total.
  - Top categories.
- Allow configuration of:
  - Default currency.
  - Data file path.
  - Pre-defined category list.

---

### Capstone B – Inventory Management Tool (Week 10)

**Goal**: Build an inventory management CLI with strong dictionary and validation usage.

**Required Folder Structure**
- `inventory_app/`
  - `__init__.py`.
  - `cli.py` – CLI user interaction (menus, prompts).
  - `inventory.py` – core operations on inventory data (add, update, list, value).
  - `validators.py` – reusable input validation functions.
  - `config.py` – initial stock and configuration (e.g., low-stock threshold).
  - `tests/` – tests for `inventory` and `validators`.

**Functional Requirements**
- In-memory inventory:
  - Use a dictionary keyed by unique product ID (string or int).
  - Each product at least includes:
    - Name.
    - Quantity (integer).
    - Price per unit (float).
  - Optional fields: category, description.
- Core operations:
  - Add a product:
    - Ensure product ID is unique or handle collision clearly.
  - Update stock:
    - Increase or decrease quantity.
  - View inventory:
    - Show list of all products with quantities and values.
  - Calculate:
    - Total inventory value (sum of `quantity * price` for all products).

**Validation & Config**
- `validators.py`:
  - Functions like `validate_quantity`, `validate_price`, `validate_product_id`.
  - Called from CLI or services, not duplicated logic.
- `config.py`:
  - Low-stock warning threshold.
  - Optional initial inventory data.

**Non-Functional Requirements**
- Clear layering:
  - `cli.py` contains all user interaction.
  - `inventory.py` only contains business logic and relies on data passed in.
- Tests:
  - Unit tests for:
    - Adding products.
    - Updating quantity (including boundary cases).
    - Calculating total value.
- Logging (optional but encouraged):
  - Important events and low-stock warnings.

**Acceptance Criteria**
- Core features (add/update/list/value) operate correctly and are demonstrable.
- Input is validated and errors are clearly communicated.
- Inventory logic is accessible through functions suitable for testing.
- At least some tests exist and pass.

**Suggested Extensions**
- Persistent storage in JSON or CSV for inventory.
- Search/filter:
  - By category.
  - By price range.
- Low-stock alert:
  - When listing, highlight items below the configured threshold.

---

### Alternative Capstone Concepts (Optional)

If the course uses alternative capstones, they must follow the same architecture and quality principles as above.

**Log Analyzer**
- **Goal**: Analyze log files for metrics and errors.
- **Requirements**:
  - Read log file(s) from disk.
  - Parse each line into a structured record (timestamp, level, message).
  - Provide summary statistics (e.g., count by level, errors per time window).
- **Acceptance Criteria**:
  - Malformed lines are handled gracefully (skipped with a log, not a crash).
  - Parsing and analysis are separate from file I/O and CLI.

**Student Result Processing System**
- **Goal**: Produce grades, ranks, and pass/fail statuses.
- **Requirements**:
  - Input: Data on students and scores.
  - Output: Grades based on clear rules, ranks, pass/fail, and optionally honors.
- **Acceptance Criteria**:
  - Grading rules are documented and implemented consistently.
  - Ranking handles ties in a deterministic way.
  - Core functions tested with several input datasets.

**Banking Simulation**
- **Goal**: Simulate basic banking operations safely.
- **Requirements**:
  - Account representation with balances.
  - Operations: deposit, withdraw, transfer.
  - Rules:
    - No negative balances.
    - Simple daily/transaction limits (optional).
- **Acceptance Criteria**:
  - All operations respect invariants (no negative balances).
  - Invalid operations are rejected with clear errors and no data corruption.
  - Logging and testing for core transaction functions.

