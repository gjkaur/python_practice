## Level 3 – Mini Project and Capstone Specifications

This document defines detailed specifications for all mini projects (MP01–MP10) and capstones, aligned with the Level 3 roadmap and PCPP-32-101.

Each project includes:
- **Goal**: What the student should learn.
- **Requirements**: Scope and must-have behaviors.
- **Acceptance Criteria**: What "done" looks like.
- **Suggested Extensions**: Optional challenges for fast learners.
- **PCPP Objectives**: Explicit mapping to PCPP-32-101 objectives.

---

### MP01 – OOP Class Hierarchy with Magic Methods (Weeks 1–2)

**Goal**: Design a class hierarchy demonstrating inheritance, polymorphism, and magic methods.

**PCPP Objectives**: 1.1, 1.2, 1.3

**Requirements**
- Design a class hierarchy with at least 3 levels (e.g., `Vehicle` → `Car` → `ElectricCar`).
- Implement at least 5 magic methods:
  - `__init__()`: proper initialization with instance and class variables.
  - `__str__()` and `__repr__()`: user-friendly and developer-friendly representations.
  - `__eq__()`: comparison based on meaningful attributes.
  - `__lt__()` or `__gt__()`: ordering (e.g., by price, year, or ID).
  - `__len__()` or `__getitem__()`: make objects behave like containers if appropriate.
- Use `isinstance()` and `issubclass()` in at least one function.
- Demonstrate polymorphism: function that works with any object in the hierarchy.

**Acceptance Criteria**
- All classes properly initialized with `__init__()`.
- Magic methods work correctly: `str(obj)`, `obj1 == obj2`, `obj1 < obj2`, etc.
- `isinstance()` and `issubclass()` used correctly.
- Polymorphic function demonstrates duck typing or inheritance-based polymorphism.
- Code follows PEP 8 and includes docstrings.

**Suggested Extensions**
- Add `@functools.total_ordering` to reduce comparison method boilerplate.
- Implement `__hash__()` to make objects hashable (if `__eq__` is defined).
- Add `__add__()` or other numeric magic methods if applicable to the domain.

---

### MP02 – Decorator Library (Week 3)

**Goal**: Create a library of reusable decorators demonstrating advanced decorator patterns.

**PCPP Objectives**: 1.4

**Requirements**
- Implement at least 4 decorators:
  - `@timer`: measures and logs function execution time.
  - `@retry(max_attempts)`: retries function on failure (decorator with arguments).
  - `@validate_input(validator_func)`: validates function arguments before execution.
  - `@cache`: caches function results (simple dictionary-based cache).
- At least one decorator must accept arguments (three-level function).
- At least one decorator must be implemented as a class (using `__call__`).
- Use `@functools.wraps` to preserve function metadata.
- Demonstrate decorator stacking: `@timer @retry(3) def func(): ...`

**Acceptance Criteria**
- All decorators work correctly and preserve function behavior.
- Decorator with arguments works: `@retry(3)`.
- Class-based decorator works: `@Logger('module')`.
- Decorator stacking works without conflicts.
- Functions retain their original names and docstrings (use `@wraps`).

**Suggested Extensions**
- Implement `@rate_limit(calls_per_second)` decorator.
- Create a decorator that logs function calls with arguments and return values.
- Implement `@deprecated(reason)` decorator that warns when deprecated function is called.

---

### MP03 – Abstract Base Class Framework (Week 4)

**Goal**: Design and implement an abstract base class system with multiple inheritance.

**PCPP Objectives**: 1.5, 1.6

**Requirements**
- Define at least 2 abstract base classes (using `abc.ABC` or `metaclass=abc.ABCMeta`):
  - Each ABC must have at least 2 abstract methods.
  - Example: `Drawable` (with `draw()`, `get_area()`), `Movable` (with `move()`, `get_position()`).
- Create at least 3 concrete classes implementing these ABCs:
  - At least one class implements multiple ABCs (multiple inheritance).
  - All abstract methods must be implemented.
- Use `@classmethod` for at least one factory method (alternative constructor).
- Use `@staticmethod` for at least one utility method.
- Demonstrate that abstract classes cannot be instantiated directly.

**Acceptance Criteria**
- Abstract classes cannot be instantiated (raises `TypeError`).
- All concrete classes successfully implement all abstract methods.
- Multiple inheritance works correctly (MRO resolves methods properly).
- Factory methods create instances correctly.
- Code uses proper type hints and docstrings.

**Suggested Extensions**
- Add abstract properties using `@property` with `@abstractmethod`.
- Implement a registry pattern where all concrete classes are automatically registered.
- Create a mixin class that provides common functionality to multiple ABCs.

---

### MP04 – Encapsulated Class Design (Week 5)

**Goal**: Implement classes with proper encapsulation using properties and subclass built-ins.

**PCPP Objectives**: 1.7, 1.8

**Requirements**
- Create at least 2 classes demonstrating encapsulation:
  - Class 1: Use `@property` with getter, setter, and deleter for at least one attribute.
  - Class 2: Subclass a built-in class (e.g., `list`, `dict`, `str`) and extend/modify behavior.
- Property setter must include validation (e.g., range checks, type checks).
- Property deleter must handle cleanup appropriately.
- Subclass must override at least 2 methods from the parent built-in class.
- Demonstrate that encapsulation prevents invalid states.

**Acceptance Criteria**
- Properties work correctly: `obj.attr = value` calls setter, `del obj.attr` calls deleter.
- Validation in setters prevents invalid values (raises `ValueError` or similar).
- Subclass behaves like parent but with extended/modified functionality.
- Code demonstrates "has a" vs "is a" relationships appropriately.
- All classes have proper docstrings explaining encapsulation strategy.

**Suggested Extensions**
- Implement a custom `__setattr__` to enforce encapsulation rules.
- Create a class that subclasses multiple built-ins (if conceptually valid).
- Add `__slots__` to optimize memory usage for classes with fixed attributes.

---

### MP05 – Exception Handling System (Week 6)

**Goal**: Build a robust exception handling system with chained exceptions and traceback analysis.

**PCPP Objectives**: 1.9, 1.10

**Requirements**
- Define a custom exception hierarchy (at least 3 exception classes).
- Implement exception chaining:
  - At least one example of implicit chaining (`raise` in `except` block).
  - At least one example of explicit chaining (`raise NewException from OriginalException`).
- Create a function that analyzes exception tracebacks:
  - Extracts traceback information using `traceback` module.
  - Logs formatted traceback to file.
  - Returns structured error information.
- Demonstrate shallow and deep copy:
  - Create a class with nested mutable attributes.
  - Show difference between `copy.copy()` and `copy.deepcopy()`.
  - Demonstrate when shallow copy causes bugs.

**Acceptance Criteria**
- Custom exception hierarchy is logical and follows inheritance.
- Exception chaining preserves error context (visible in traceback).
- Traceback analysis function extracts and formats information correctly.
- Copy operations demonstrate clear difference between shallow and deep.
- All exceptions include meaningful error messages.

**Suggested Extensions**
- Implement a context manager that automatically logs exceptions with tracebacks.
- Create a decorator that wraps functions with exception handling and chaining.
- Implement custom `__copy__` and `__deepcopy__` methods for a class.

---

### MP06 – Object Persistence System (Week 7)

**Goal**: Implement object serialization using pickle and shelve, and explore metaprogramming.

**PCPP Objectives**: 1.11, 1.12

**Requirements**
- Create a class that can be pickled and unpickled:
  - Class with instance variables, including nested objects (lists, dicts, other custom objects).
  - Demonstrate `pickle.dumps()`/`loads()` and `pickle.dump()`/`load()`.
  - Handle pickling errors gracefully.
- Implement a simple database using `shelve`:
  - Store and retrieve objects by key.
  - Implement at least 3 operations: `save(key, obj)`, `load(key)`, `delete(key)`.
  - Handle missing keys appropriately.
- Create a simple metaclass example:
  - Metaclass that adds a method or attribute to all classes that use it.
  - At least one class uses this metaclass.
  - Demonstrate accessing `__name__`, `__bases__`, `__dict__` programmatically.

**Acceptance Criteria**
- Objects can be pickled and unpickled successfully (round-trip works).
- Shelve database stores and retrieves objects correctly.
  - Missing keys handled with appropriate exceptions or default values.
- Metaclass modifies class creation as intended.
- Special attributes (`__name__`, `__bases__`, `__dict__`) accessed correctly.
- Code includes error handling for serialization failures.

**Suggested Extensions**
- Implement custom `__getstate__` and `__setstate__` for complex pickling.
- Create a registry metaclass that automatically registers all subclasses.
- Build a simple ORM-like system using shelve with query methods.

---

### MP07 – Code Quality Refactor (Week 8)

**Goal**: Refactor existing code to meet PEP 8, PEP 257, and type hint standards.

**PCPP Objectives**: 2.1, 2.2, 2.3

**Requirements**
- Select a previous mini project (MP01–MP06) or provided "messy" code.
- Apply PEP 8 guidelines:
  - Fix indentation, line length, imports, naming conventions.
  - Use automated tools: `black`, `flake8`, or `autopep8`.
- Add PEP 257 docstrings:
  - Module-level docstring.
  - Class docstrings (one-line or multi-line as appropriate).
  - Function/method docstrings with parameter and return descriptions.
- Add type hints (PEP 484):
  - Function parameters and return types.
  - Use `typing` module for complex types (`List`, `Dict`, `Optional`, `Union`).
  - Run `mypy` to check type hints (optional but encouraged).
- Document the refactoring process:
  - List of changes made.
  - Before/after code snippets for key improvements.

**Acceptance Criteria**
- Code passes `flake8` (or equivalent) with no errors (warnings acceptable if justified).
- All public functions, classes, and modules have docstrings.
- Type hints added to all function signatures.
- Code is more readable and maintainable after refactoring.
- Refactoring document explains improvements clearly.

**Suggested Extensions**
- Set up pre-commit hooks to automatically check code quality.
- Create a style guide document for the project.
- Add Sphinx documentation generation from docstrings.

---

### MP08 – GUI Calculator or Todo App (Week 9)

**Goal**: Build a functional GUI application using tkinter with event-driven programming.

**PCPP Objectives**: 3.1, 3.2, 3.3

**Requirements**
- Create a GUI application (choose one):
  - **Option A**: Calculator with basic operations (+, -, *, /) and clear/reset.
  - **Option B**: Todo list app with add, delete, mark complete, and list display.
- GUI must include:
  - Main window with title and proper sizing.
  - At least 5 different widget types: `Label`, `Button`, `Entry`, `Listbox` or `Text`, and one of `Radiobutton`/`Checkbutton`.
  - Use `grid()` layout manager (primary) with proper spacing.
  - Event handlers for all interactive elements.
- Implement observable variables:
  - Use `StringVar` or `IntVar` for at least one widget.
  - Demonstrate variable tracing (optional but encouraged).
- Input validation and error handling:
  - Validate user input (e.g., numeric input for calculator).
  - Display user-friendly error messages in GUI (not console).

**Acceptance Criteria**
- Application launches and displays correctly.
- All buttons and interactions work as expected.
- Input validation prevents invalid operations.
- Error messages displayed in GUI (e.g., messagebox or label).
- Code is organized: separate GUI setup from event handlers.
- Application closes cleanly (handles window close event).

**Suggested Extensions**
- Add keyboard shortcuts (e.g., Enter to calculate/submit).
- Implement a menu bar with File/Edit menus.
- Add a settings dialog using `Toplevel` window.
- Use `Canvas` widget to draw something (e.g., graph for calculator history).

---

### MP09 – REST API Client (Week 10)

**Goal**: Build a REST client that communicates with a web API using `requests` and handles JSON/XML.

**PCPP Objectives**: 4.1, 4.2, 4.3, 4.4

**Requirements**
- Create a REST client class that implements CRUD operations:
  - `get(resource, id=None)`: GET request to fetch data.
  - `create(resource, data)`: POST request to create new resource.
  - `update(resource, id, data)`: PUT request to update resource.
  - `delete(resource, id)`: DELETE request to delete resource.
- Handle JSON data:
  - Serialize Python objects to JSON for requests.
  - Deserialize JSON responses to Python objects.
  - Handle JSON errors gracefully.
- Implement error handling:
  - Check HTTP status codes (2xx success, 4xx client error, 5xx server error).
  - Raise custom exceptions for different error types.
  - Retry logic for transient failures (optional but encouraged).
- Use a real API or mock server:
  - JSONPlaceholder (https://jsonplaceholder.typicode.com) or similar.
  - Or create a simple Flask/FastAPI mock server (extension).

**Acceptance Criteria**
- All CRUD operations work correctly with the API.
- JSON serialization/deserialization handles Python types correctly.
- Error handling provides meaningful messages for different failure scenarios.
- Code uses `requests` library appropriately (not raw sockets).
- Client class is reusable and well-documented.

**Suggested Extensions**
- Add pagination support for list endpoints.
- Implement authentication (API keys or OAuth tokens).
- Add request/response logging.
- Parse XML responses (if API supports XML).
- Create a simple CLI interface to interact with the REST client.

---

### MP10 – Database-Backed Application (Week 11)

**Goal**: Build an application with SQLite database, file processing, and logging.

**PCPP Objectives**: 5.1, 5.2

**Requirements**
- Create a database-backed application (choose domain: library, inventory, contacts, etc.):
  - At least 2 related tables with foreign key relationships.
  - Implement full CRUD operations for both tables.
  - Use parameterized queries to prevent SQL injection.
  - Implement transactions for multi-step operations.
- File processing:
  - Import data from CSV file into database.
  - Export data from database to CSV file.
  - Use `csv.DictReader` and `csv.DictWriter`.
- Logging:
  - Set up logging with at least 2 handlers (file and console).
  - Use different log levels: `INFO` for operations, `ERROR` for failures.
  - Custom formatter with timestamp, level, and message.
- Configuration:
  - Use `ConfigParser` to read database path, log file path, and other settings from `.ini` file.
  - Application reads config on startup.

**Acceptance Criteria**
- Database operations work correctly (create, read, update, delete).
- Foreign key relationships enforced (or handled gracefully).
- CSV import/export works without data loss.
- Logging writes to both file and console with appropriate levels.
- Configuration file is read correctly, application fails gracefully if missing.
- Code uses proper error handling for database and file operations.

**Suggested Extensions**
- Add database migration system (simple version tracking).
- Implement search/filter functionality with SQL `LIKE` or full-text search.
- Add logging rotation (using `RotatingFileHandler`).
- Create a simple CLI interface for the application.
- Add data validation before database insertion.

---

### Capstone 1 – Full-Stack GUI Application with Database (Week 12)

**Goal**: Build a complete GUI application integrating OOP, GUI, database, logging, and configuration.

**PCPP Objectives**: All sections (1.1–5.2)

**Required Folder Structure**
```
capstone_gui_app/
├── __init__.py
├── main.py                 # Application entry point
├── models.py               # Data models (OOP classes)
├── database.py             # Database operations (sqlite3)
├── services.py             # Business logic layer
├── gui/
│   ├── __init__.py
│   ├── main_window.py      # Main GUI window
│   ├── dialogs.py          # Dialog windows
│   └── widgets.py          # Custom widgets
├── config.py               # Configuration management (ConfigParser)
├── logging_config.py       # Logging setup
├── tests/                  # Unit tests
│   ├── test_models.py
│   ├── test_services.py
│   └── test_database.py
├── config.ini              # Configuration file
└── README.md               # Project documentation
```

**Functional Requirements**
- **Domain**: Choose one (or propose alternative):
  - Personal Finance Manager: track income/expenses, budgets, categories.
  - Library Management System: manage books, members, loans.
  - Task/Project Manager: projects, tasks, deadlines, priorities.
  - Inventory Management: products, suppliers, stock levels.
- **Core Features**:
  - Full CRUD operations via GUI (create, read, update, delete records).
  - Data validation in GUI and business logic layers.
  - Search/filter functionality.
  - Data persistence in SQLite database.
  - Export data to CSV.
- **GUI Requirements**:
  - Main window with menu bar and toolbar (optional).
  - Forms for data entry (using `Entry`, `Text`, `Radiobutton`, `Checkbutton`).
  - List/table display of records (`Listbox` or `Treeview`).
  - Dialog windows for confirmations and detailed views.
  - Status bar showing application state.
- **Database Requirements**:
  - At least 2 related tables with foreign keys.
  - Proper schema with constraints (PRIMARY KEY, FOREIGN KEY, NOT NULL, etc.).
  - Transaction support for data integrity.
- **Non-Functional Requirements**:
  - Separation of concerns: GUI, services, database layers clearly separated.
  - Logging: all important operations and errors logged.
  - Configuration: database path, UI settings, etc. in `.ini` file.
  - Error handling: user-friendly error messages, no crashes.
  - Code quality: PEP 8, PEP 257 docstrings, type hints.

**Acceptance Criteria**
- Application runs without errors and provides all required functionality.
- GUI is responsive and user-friendly.
- Database operations are correct and efficient.
- Code follows MVC or similar architectural pattern.
- All layers (GUI, services, database) are testable independently.
- Logging captures important events and errors.
- Configuration is externalized and documented.
- README explains installation, usage, and architecture.

**Suggested Extensions**
- Add data visualization (charts/graphs) using `matplotlib` or similar.
- Implement undo/redo functionality.
- Add keyboard shortcuts for common operations.
- Create installer or packaging for distribution.
- Add user authentication and multi-user support.
- Implement data backup/restore functionality.

---

### Capstone 2 – REST Client with GUI Frontend (Week 12)

**Goal**: Build a REST API client with GUI frontend, integrating network programming, GUI, and data persistence.

**PCPP Objectives**: All sections (1.1–5.2)

**Required Folder Structure**
```
capstone_rest_client/
├── __init__.py
├── main.py                 # Application entry point
├── models.py               # Data models
├── api_client.py           # REST client (requests)
├── cache.py                # Local caching (shelve or sqlite)
├── gui/
│   ├── __init__.py
│   ├── main_window.py      # Main GUI
│   ├── request_builder.py  # GUI for building requests
│   └── response_viewer.py  # Display responses
├── config.py               # Configuration (API endpoints, keys)
├── logging_config.py       # Logging setup
├── tests/
│   ├── test_api_client.py
│   └── test_models.py
├── config.ini              # Configuration file
└── README.md
```

**Functional Requirements**
- **REST Client**:
  - Support for GET, POST, PUT, DELETE methods.
  - Request builder: GUI form to construct requests (URL, method, headers, body).
  - Response viewer: display response status, headers, body (formatted JSON/XML/text).
  - Handle authentication: API keys, Bearer tokens (stored securely in config).
- **GUI Features**:
  - Main window with request/response panes.
  - Request builder: URL input, method selector, headers table, body editor.
  - Response viewer: status code, headers display, formatted body (syntax highlighting if possible).
  - History: save recent requests/responses (persist to database or file).
  - Favorites: save frequently used requests.
- **Data Persistence**:
  - Cache API responses locally (using `shelve` or SQLite).
  - Save request history to database.
  - Export/import request collections (JSON format).
- **Error Handling**:
  - Network errors displayed in GUI.
  - Invalid JSON/XML handled gracefully.
  - Timeout handling with user feedback.

**Acceptance Criteria**
- REST client successfully communicates with real APIs (e.g., JSONPlaceholder, GitHub API).
- GUI allows building and sending requests easily.
- Responses are displayed in readable format.
- Request history is saved and can be recalled.
- Caching reduces redundant API calls.
- Error handling provides clear feedback.
- Code is well-structured with separation of concerns.
- Configuration management works correctly.

**Suggested Extensions**
- Add support for WebSocket connections.
- Implement OAuth 2.0 authentication flow.
- Add request/response validation against OpenAPI/Swagger specs.
- Create collections/environments (like Postman).
- Add scripting support for automated testing.
- Implement response comparison/diff functionality.

---

### Alternative Capstone Concepts

If students want to propose alternative capstones, they must integrate at least 3 of the 5 PCPP sections:

**Option A – Data Analysis Tool**
- GUI for loading CSV/JSON data.
- Database for storing datasets.
- REST API integration for fetching external data.
- Visualization using matplotlib (extension).

**Option B – Chat Application**
- GUI client interface.
- Network programming (sockets or REST API).
- Database for message history.
- Object serialization for message objects.

**Option C – Configuration Management Tool**
- GUI for editing configuration files.
- Database for configuration versioning.
- REST API for remote configuration sync.
- File processing (INI, JSON, XML, CSV).

All alternative capstones must meet the same non-functional requirements (PEP 8, logging, error handling, documentation) as the primary capstones.

---

This completes the project specifications for Level 3, covering all PCPP-32-101 objectives through practical, real-world projects.
