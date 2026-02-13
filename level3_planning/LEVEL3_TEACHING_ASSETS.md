## Level 3 – Teaching Assets and Supporting Materials

This document outlines practical teaching aids to support the Level 3 course:
- Starter code templates.
- Code review checklists.
- Sample Git workflows for advanced projects.
- Additional teaching resources (cheat sheets, refactor walkthroughs, question banks).

---

### 1. Starter Templates

These templates can be stored in a `templates/` folder or shared per module.

#### 1.1 OOP Class Template (`oop_class_template.py`)

Purpose: Provide a standard pattern for classes with magic methods and proper structure.

Suggested structure:
- Class with `__init__`, `__str__`, `__repr__`, `__eq__`.
- Class variables and instance variables clearly separated.
- Docstrings for class and methods.
- Type hints for methods.

Usage:
- Students copy this when starting MP01 or any OOP-focused project.

#### 1.2 Decorator Template (`decorator_template.py`)

Purpose: Show patterns for function decorators, decorators with arguments, and class decorators.

Suggested contents:
- Simple function decorator with `@functools.wraps`.
- Decorator with arguments (three-level function).
- Class-based decorator with `__call__`.
- Examples of decorator stacking.

Usage:
- Base for MP02 (Decorator Library).

#### 1.3 Abstract Base Class Template (`abc_template.py`)

Purpose: Demonstrate abstract class structure with `abc` module.

Suggested contents:
- Abstract base class using `abc.ABC`.
- Abstract methods with `@abstractmethod`.
- Concrete implementation class.
- Example of multiple inheritance from ABCs.

Usage:
- Used in MP03 (Abstract Base Class Framework).

#### 1.4 Property Template (`property_template.py`)

Purpose: Show encapsulation using `@property` decorator.

Suggested contents:
- Class with private attribute (`_attr`).
- Property with getter, setter, deleter.
- Validation in setter.
- Computed property example.

Usage:
- Used in MP04 (Encapsulated Class Design).

#### 1.5 tkinter App Template (`tkinter_app_template.py`)

Purpose: Provide skeleton for GUI applications.

Suggested structure:
- Main window class inheriting from `tk.Tk` or using composition.
- Methods for widget creation, event handlers.
- Layout using `grid()` manager.
- Observable variables (`StringVar`, `IntVar`).
- Menu bar structure (optional).

Usage:
- Base for MP08 (GUI Calculator/Todo App) and capstones.

#### 1.6 REST Client Template (`rest_client_template.py`)

Purpose: Standard structure for REST API clients.

Suggested contents:
- `RESTClient` class with `__init__` (base URL, headers).
- Methods: `get()`, `post()`, `put()`, `delete()`.
- Error handling with custom exceptions.
- JSON serialization/deserialization helpers.

Usage:
- Base for MP09 (REST API Client) and Capstone 2.

#### 1.7 Database Template (`database_template.py`)

Purpose: SQLite database connection and CRUD operations pattern.

Suggested contents:
- Database connection context manager.
- Base class for database operations.
- Example CRUD methods with parameterized queries.
- Transaction handling.

Usage:
- Base for MP10 (Database-Backed Application) and capstones.

#### 1.8 Project Structure Template (`project_structure_template/`)

Purpose: Provide ready-to-use skeleton for capstones.

Example layout:
```
project_name/
├── __init__.py
├── main.py              # Entry point
├── models.py            # Data models
├── services.py          # Business logic
├── database.py          # Database operations
├── config.py           # Configuration
├── logging_config.py    # Logging setup
├── gui/                # GUI package (if applicable)
│   ├── __init__.py
│   └── main_window.py
├── tests/              # Test package
│   ├── __init__.py
│   ├── test_models.py
│   └── test_services.py
├── config.ini          # Configuration file
└── README.md           # Project documentation
```

Usage:
- Students clone/copy this structure for capstones.

---

### 2. Code Review Checklists

#### 2.1 Student Self-Review Checklist

Before submitting, students should ask:

- **Correctness**
  - Have I tested all core functionality?
  - Do edge cases work correctly?
  - Are there any obvious bugs or crashes?

- **PCPP Objective Coverage**
  - Have I used the required PCPP concepts (magic methods, decorators, etc.)?
  - Are concepts used correctly, not just superficially?

- **OOP Design**
  - Is my class hierarchy logical?
  - Am I using inheritance appropriately (not overusing it)?
  - Are magic methods used where they make sense?
  - Is encapsulation proper (properties, private attributes)?

- **Code Quality**
  - Does my code follow PEP 8?
  - Do all public functions/classes have docstrings (PEP 257)?
  - Have I added type hints (PEP 484)?
  - Is code readable without comments?

- **Error Handling**
  - Are exceptions handled appropriately?
  - Are error messages user-friendly?
  - Is logging used for important events?

- **Testing**
  - Do I have tests for core logic?
  - Are tests meaningful (not just trivial assertions)?

- **Git**
  - Did I commit incrementally with descriptive messages?
  - Is my commit history clean and logical?

#### 2.2 Peer/Instructor Review Checklist

Guided questions:

- **Readability & Style**
  - Can I understand the code without running it?
  - Are docstrings clear and complete?
  - Do type hints help or hinder readability?

- **OOP Design**
  - Is the class hierarchy well-designed?
  - Are magic methods used appropriately?
  - Is there proper separation of concerns?

- **Robustness**
  - Does the code handle errors gracefully?
  - Are edge cases considered?
  - Is logging used appropriately?

- **PCPP Mastery**
  - Does the code demonstrate understanding of advanced concepts?
  - Are decorators, abstract classes, etc. used correctly?
  - Could this code be improved with more advanced patterns?

- **Testability**
  - Is the code structured for testing?
  - Are there tests, and do they cover important paths?

Reviewers should leave:
- At least one positive comment (something done well).
- 2–3 specific suggestions for improvement.
- Reference to relevant PCPP objectives if applicable.

---

### 3. Sample Git Workflows for Advanced Projects

#### 3.1 Feature Branch Workflow (Weeks 1–7)

Focus: Develop features in isolation, merge when complete.

Suggested pattern:
- Create branch for each mini project: `git checkout -b feature/mp02-decorators`.
- Develop feature with multiple commits:
  - `git commit -m "Add basic timer decorator"`
  - `git commit -m "Add retry decorator with arguments"`
  - `git commit -m "Add class-based logger decorator"`
- Merge to main: `git checkout main`, `git merge feature/mp02-decorators`.
- Delete branch: `git branch -d feature/mp02-decorators`.

Teaching emphasis:
- Keep `main` branch stable.
- Use branches for experimentation.
- Write descriptive commit messages.

#### 3.2 Capstone Workflow (Weeks 8–12)

Focus: Long-term project with multiple features and iterations.

Suggested pattern:
- Main branch: `main` (stable, deployable).
- Development branch: `develop` (integration branch).
- Feature branches: `feature/gui-main-window`, `feature/database-schema`, etc.
- Release branches: `release/v1.0` (preparing for release).

Workflow:
1. Create feature branch from `develop`.
2. Develop and commit incrementally.
3. Merge feature to `develop` when complete.
4. Merge `develop` to `main` for releases.
5. Tag releases: `git tag -a v1.0 -m "Initial release"`.

Teaching emphasis:
- Organizing work over weeks.
- Using branches for parallel development.
- Tagging milestones for project history.

#### 3.3 Code Review Workflow

For capstones, simulate pull request workflow:
- Create feature branch.
- Push to remote (GitHub/GitLab).
- Create pull request (or merge request).
- Peer/instructor reviews.
- Address feedback, push updates.
- Merge after approval.

Teaching emphasis:
- Professional collaboration practices.
- Code review as learning opportunity.
- Iterative improvement based on feedback.

---

### 4. Additional Teaching Resources

#### 4.1 Concept Cheat Sheets

Short 1–2 page references for:

- **Magic Methods Quick Reference**
  - Comparison: `__eq__`, `__lt__`, `__le__`, `__gt__`, `__ge__`, `__ne__`.
  - Numeric: `__add__`, `__sub__`, `__mul__`, `__truediv__`, `__abs__`, etc.
  - Container: `__getitem__`, `__setitem__`, `__len__`, `__contains__`, `__iter__`.
  - Representation: `__str__`, `__repr__`, `__bool__`.
  - Attribute access: `__getattr__`, `__setattr__`, `__getattribute__`.

- **Decorator Patterns**
  - Simple decorator syntax.
  - Decorator with arguments pattern.
  - Class decorator pattern.
  - Common decorators: `@property`, `@staticmethod`, `@classmethod`, `@abstractmethod`.

- **tkinter Widgets Reference**
  - Common widgets: `Label`, `Button`, `Entry`, `Text`, `Listbox`, `Canvas`.
  - Layout managers: `pack()`, `grid()`, `place()`.
  - Events: `<Button-1>`, `<Key>`, `<Return>`, etc.
  - Observable variables: `StringVar`, `IntVar`, `BooleanVar`.

- **SQLite Quick Reference**
  - Connection: `sqlite3.connect()`, `connection.close()`.
  - Cursor: `cursor.execute()`, `cursor.fetchone()`, `cursor.fetchall()`.
  - Transactions: `connection.commit()`, `connection.rollback()`.
  - Common SQL: `SELECT`, `INSERT`, `UPDATE`, `DELETE`, `CREATE TABLE`.

- **requests Module Quick Reference**
  - Methods: `requests.get()`, `requests.post()`, `requests.put()`, `requests.delete()`.
  - Parameters: `params`, `json`, `headers`, `timeout`.
  - Response: `response.status_code`, `response.text`, `response.json()`, `response.headers`.

Format:
- Markdown or PDF, linked from course README or LMS.
- Printable for quick reference during coding.

#### 4.2 Refactor Walkthroughs

Step-by-step examples showing:

- **Adding Magic Methods to Existing Class**
  - Start with class without magic methods.
  - Add `__str__` and `__repr__`.
  - Add `__eq__` for comparison.
  - Add `__lt__` for ordering.
  - Show before/after code and usage.

- **Converting Functions to Decorators**
  - Start with wrapper function pattern.
  - Convert to simple decorator.
  - Add decorator arguments.
  - Convert to class decorator.
  - Show evolution step-by-step.

- **Refactoring to Use Abstract Base Classes**
  - Start with concrete classes without interface enforcement.
  - Extract common interface to ABC.
  - Make classes inherit from ABC.
  - Show how ABC prevents incomplete implementations.

- **Converting CLI to GUI**
  - Start with CLI application.
  - Identify user interactions.
  - Design GUI layout.
  - Convert input/output to GUI widgets.
  - Show event-driven structure.

Use cases:
- Used in Modules 1–9 to demonstrate professional code evolution.
- Show how to improve code incrementally.

#### 4.3 Practice Question Bank

Categories aligned with PCPP objectives:

- **Concept Questions**
  - "Explain the difference between `@staticmethod` and `@classmethod`. Provide examples of when to use each."
  - "What is Method Resolution Order (MRO)? How does Python resolve method calls in multiple inheritance?"
  - "Explain the difference between shallow copy and deep copy. When would you use each?"

- **Code Analysis Questions**
  - Given code with magic methods, predict output.
  - Identify which magic method is called for specific operations.
  - Debug code with decorator issues.

- **Design Questions**
  - "Design a class hierarchy for a drawing application. Should `Circle` inherit from `Shape` or use composition? Justify your choice."
  - "Design a REST client class. What methods should it have? How would you handle errors?"

- **Debugging Tasks**
  - "This code raises a `TypeError` when pickling. Why? How can you fix it?"
  - "This GUI freezes when making a network request. What's wrong? How would you fix it?"

Usage:
- Used for quizzes, homework, or exam preparation.
- Can be used for interview-style practice.

#### 4.4 Lesson Slide Outlines or Whiteboard Prompts

For instructors:

- **Module 1 (OOP Foundations)**
  - Key terms: class, instance, object, attribute, method, inheritance, polymorphism.
  - Diagram: class hierarchy example.
  - Live coding: build a class hierarchy step-by-step.

- **Module 2 (Magic Methods)**
  - Table: operation → magic method (e.g., `==` → `__eq__`).
  - Live coding: add magic methods to existing class.
  - Common mistakes: forgetting `@functools.wraps` in decorators.

- **Module 3 (Decorators)**
  - Diagram: decorator execution flow.
  - Live coding: build decorator from scratch.
  - Pattern: three-level function for decorator with arguments.

- **Module 9 (GUI)**
  - Diagram: event-driven programming flow.
  - Live coding: build simple GUI step-by-step.
  - Common mistakes: blocking operations in GUI thread.

For students:
- PDF exports or screenshots of key diagrams shared in repo or class portal.
- Mermaid diagrams for architecture (class hierarchies, component interactions).

#### 4.5 Debugging Guides

Common issues and solutions:

- **Magic Methods Not Working**
  - Check method name spelling (double underscores).
  - Ensure method is defined in correct class.
  - Check if method should return specific type.

- **Decorator Issues**
  - Function loses name/docstring → use `@functools.wraps`.
  - Decorator with arguments not working → check three-level function structure.
  - Decorator stacking order → remember bottom-to-top application.

- **GUI Freezing**
  - Blocking operation in main thread → use `after()` or threading.
  - Infinite loop in event handler → check loop conditions.

- **Database Connection Issues**
  - Database locked → ensure connections are closed.
  - Transaction not committing → call `commit()` explicitly.
  - SQL injection risk → always use parameterized queries.

- **Network Request Failures**
  - Connection timeout → increase timeout or handle exception.
  - JSON decode error → check response content type.
  - Status code not checked → always verify `response.status_code`.

Format:
- Troubleshooting guide document.
- Common error messages and solutions.
- Links to relevant documentation.

---

### 5. Assessment Tools

#### 5.1 Automated Code Quality Checks

Tools to integrate:

- **flake8**: PEP 8 compliance checking.
  - Configuration: `.flake8` file with ignored rules if needed.
  - Pre-commit hook: run `flake8` before commits.

- **black**: Code formatting (optional, but widely adopted).
  - Configuration: `pyproject.toml` with line length, etc.
  - Can be run manually or integrated into IDE.

- **mypy**: Type checking (PEP 484).
  - Configuration: `mypy.ini` with strictness settings.
  - Gradual typing: start lenient, increase strictness.

- **pylint**: Comprehensive linting (optional).
  - More opinionated than flake8.
  - Can be configured to match team standards.

Setup instructions:
- Add to project README.
- Provide example configuration files.
- Show how to run in CI/CD (if applicable).

#### 5.2 Test Framework Setup

Templates for:

- **unittest**: Standard library testing.
  - Test class structure.
  - Assertion methods.
  - Mocking examples.

- **pytest**: Popular third-party framework (optional).
  - Simpler syntax.
  - Fixtures for setup/teardown.
  - Parametrized tests.

Test templates:
- `test_template.py` with example test cases.
- Mock examples for database, network calls.
- Integration test patterns.

---

### 6. Project Management Templates

#### 6.1 Project Proposal Template

For capstones, students should submit a proposal:

- **Project Title and Description**
- **Objectives**: Which PCPP objectives will be covered?
- **Features**: List of core features and optional extensions.
- **Technology Stack**: GUI framework, database, APIs, etc.
- **Architecture**: High-level design (diagram or description).
- **Timeline**: Week-by-week breakdown of work.
- **Risks and Challenges**: Potential issues and mitigation.

#### 6.2 Progress Report Template

For tracking capstone progress:

- **Week X Progress**
  - Completed: What was finished this week?
  - In Progress: What's currently being worked on?
  - Blockers: Any issues preventing progress?
  - Next Steps: Plan for next week.

#### 6.3 Final Presentation Template

For capstone presentations:

- **Problem Statement**: What problem does this solve?
- **Architecture**: How is the system designed?
- **Key Features**: Demo of main functionality.
- **Technical Highlights**: Advanced concepts used (magic methods, decorators, etc.).
- **Challenges**: What was difficult? How did you overcome it?
- **Future Improvements**: What would you add next?

---

These assets are meant to be adapted to your teaching style and learners' pace, while keeping alignment with PCPP-32-101 and professional practices targeted by the Level 3 course.
