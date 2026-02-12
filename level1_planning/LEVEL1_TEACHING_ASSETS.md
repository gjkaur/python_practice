## Level 1 – Teaching Assets and Supporting Materials

This document outlines practical teaching aids to support the Level 1 course:
- Starter code templates.
- Code review checklists.
- Sample Git workflows for students.
- Additional teaching resources (cheat sheets, refactor walkthroughs, question banks).

---

### 1. Starter Templates

These templates can be stored in a `templates/` folder or shared per module.

#### 1.1 Basic Script Template (`basic_script_template.py`)

Purpose: Give beginners a standard pattern for small scripts from Week 1 onward.

Suggested structure:
- `main()` function with a clear docstring.
- `if __name__ == "__main__": main()` guard.
- Placeholder comments indicating where to add logic.

Usage:
- Students copy this file when starting most small scripts in Modules 0–2.

#### 1.2 Menu Template (`menu_template.py`)

Purpose: Provide a reusable pattern for CLI menus (Module 2 and beyond).

Suggested contents:
- A `show_menu()` function that prints numbered options.
- A `get_choice()` helper that reads and validates user input.
- A `while` loop and `handle_choice(choice)` function that:
  - Dispatches to stub functions like `do_option_1()`, `do_option_2()`, etc.
  - Handles an `EXIT` option cleanly.

Usage:
- Base for MP4 (CLI Menu System) and reused in MP5–MP9.

#### 1.3 Collections Template (`list_dict_template.py`)

Purpose: Encourage good patterns when using lists/tuples/dicts (Module 3).

Suggested contents:
- Example list, tuple, and dictionary definitions.
- Stub functions like:
  - `add_item(collection, item)`
  - `find_item(collection, criteria)`
  - `remove_item(collection, item_id)`

Usage:
- Used in Student Score Manager and Address Book as a starting point.

#### 1.4 Function Template (`function_template.py`)

Purpose: Reinforce good function design (Module 4).

Suggested contents:
- Example pure function with:
  - Docstring explaining parameters, return type, and behavior.
  - Type hints (optional preview).
- Example of separating printing from returning values.

Usage:
- Used when refactoring older mini projects in MP7.

#### 1.5 Project Skeleton Template (`project_skeleton_template/`)

Purpose: Provide a ready-to-use skeleton for capstones and MP9.

Example layout:
- `project_skeleton/`
  - `__init__.py`
  - `main.py` (CLI entry point with stubbed `main()`).
  - `services.py` (empty or stubbed functions).
  - `storage.py` (placeholder `load_data`, `save_data`).
  - `config.py` (placeholder config loading).
  - `tests/` (empty `test_sample.py`).

Usage:
- Students clone/copy this structure for Expense Tracker, Inventory App, or other capstones.

#### 1.6 Config and Logging Templates

Purpose: Lower the barrier to using configuration and logging (Module 5+).

Assets:
- `config_example.json` or `config_example.ini`:
  - Example keys: `reminder_interval`, `default_message`, `data_file`.
- `logging_config_example.py`:
  - Minimal `logging.basicConfig(level=logging.INFO)` setup.

Usage:
- Introduced with MP9 and reused in capstones.

---

### 2. Code Review Checklists

These checklists can be printed, included in course docs, or embedded in assignment instructions.

#### 2.1 Student Self-Review Checklist

Before submitting, students should ask:
- **Correctness**
  - Have I run the program with valid and invalid inputs?
  - Do the outputs match the assignment requirements?
- **Style**
  - Are my variable and function names descriptive and in `snake_case`?
  - Are my lines reasonably short and readable?
- **Structure**
  - Are any functions too long or trying to do too much?
  - Is there duplicated logic that could be moved into a function?
- **Error Handling**
  - What happens if the user enters something unexpected?
  - Am I relying on crashes (tracebacks) instead of messages for users?
- **Git**
  - Did I make multiple commits instead of one large “dump”?
  - Are my commit messages short, descriptive, and in imperative form?

#### 2.2 Peer/Instructor Review Checklist

Guided questions:
- **Readability**
  - Can I understand what each function does without running it?
  - Are comments used to explain “why” rather than “what”?
- **Design**
  - Is I/O separated from business logic where possible?
  - Are modules/files focused on single responsibilities?
- **Robustness**
  - Does the code handle typical error conditions or edge cases gracefully?
  - Are exceptions used appropriately and specifically?
- **Testability**
  - Are there pure functions that could be tested?
  - Do any tests exist, and do they cover the important paths?

Reviewers should leave at least:
- One positive comment (something done well).
- One suggestion for improvement.

---

### 3. Sample Git Workflows for Students

#### 3.1 Beginner Workflow (Weeks 1–4)

Focus: Learn the basics of Git with local repositories.

Suggested steps:
1. Initialize repository: `git init`.
2. After making a small change:
   - `git status` to see changes.
   - `git add <file>` to stage.
   - `git commit -m "Describe your change"` to commit.
3. Repeat for each meaningful change:
   - Example messages: “Add basic menu loop”, “Implement unit conversion logic”.

Teaching emphasis:
- Commit early, commit often.
- Keep commit messages short and action-oriented.

#### 3.2 Intermediate Workflow (Weeks 5–9)

Focus: Feature branches and cleaner histories.

Suggested pattern:
- Create a branch for each project or feature:
  - `git checkout -b feature/mp5-student-score-manager`.
- Implement the feature with multiple commits.
- Merge back to main:
  - `git checkout main` then `git merge feature/mp5-student-score-manager`.

Teaching emphasis:
- Keeping `main` stable.
- Using branches for experimentation.

#### 3.3 Capstone Workflow (Week 10)

Focus: Simulate a small professional project.

Suggested pattern:
- Use separate branches for larger features (e.g., `feature/add-summary-report`).
- Create milestones or tags:
  - `v0.1-internal`, `v1.0-capstone-submission`.
- Encourage use of GitHub or similar remote for:
  - Backups.
  - Simulated pull requests and reviews.

Teaching emphasis:
- Organizing work over days/weeks.
- Using history to tell the story of a project.

---

### 4. Additional Teaching Resources

#### 4.1 Concept Cheat Sheets

Short 1–2 page references for:
- **Data Types & Literals**
  - Overview of ints, floats, bools, strings, lists, tuples, dicts.
- **Operators & Control Flow**
  - Precedence table, examples of `if/elif/else`, loops, and `for-else`.
- **Exceptions**
  - Common exception types and when they appear.
- **Logging & Config**
  - Basic logging levels and config examples.

Format:
- Markdown or PDF, linked from the course README or LMS.

#### 4.2 Refactor Walkthroughs

Step-by-step examples that show:
- Turning a long script into a set of functions.
- Replacing nested conditionals with guard clauses.
- Moving from scripts to a package structure (`main.py`, `services.py`, `storage.py`).

Use cases:
- Used in Modules 4–6 to demonstrate how professionals improve code over time.

#### 4.3 Practice Question Bank

Categories:
- **Concept Questions**
  - Example: “What is the difference between `==` and `is` in Python (at this level)?”.
- **Practical Coding Tasks**
  - Example: “Write a function that removes duplicates from a list while preserving order.”
- **Debugging Tasks**
  - Example: “Given this code that raises `IndexError`, explain the bug and fix it.”

Usage:
- Used for quizzes, homework, or interview-style practice.

#### 4.4 Lesson Slide Outlines or Whiteboard Prompts

For instructors:
- Outline per lesson with:
  - Key terms to define.
  - Example snippets to walk through live.
  - One small “live refactor” per week to model professional habits.

For students:
- PDF exports or screenshots of key diagrams (e.g., the capstone architecture mermaid diagram) shared in the repo or class portal.

---

These assets are meant to be adapted to your teaching style and learners’ pace, while keeping alignment with PCEP-30-02 and the professional practices targeted by the Level 1 course.

