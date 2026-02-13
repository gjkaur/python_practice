# Capstone 1 – Full-Stack GUI Application with Database

**PCPP Objectives**: All sections (1.1–5.2)  
**Duration**: 2-3 weeks  
**Weight**: 30% of final grade

## Goal

Build a complete desktop application integrating GUI, database, logging, and configuration management.

## Project Description

Create a desktop application of your choice (examples: Library Management System, Expense Tracker, Task Manager, Inventory System, Contact Manager). The application must integrate multiple technologies learned throughout the course.

## Requirements

### Core Functionality

Choose a domain and implement:

1. **Data Model** (PCPP 1.1–1.12):
   - At least 2 related classes with proper OOP design
   - Use inheritance, abstract classes, or composition as appropriate
   - Implement magic methods (`__str__`, `__repr__`, `__eq__`, etc.)
   - Use properties for encapsulation where appropriate

2. **Database Layer** (PCPP 5.1):
   - SQLite database with at least 2 related tables
   - Foreign key relationships
   - Full CRUD operations
   - Use parameterized queries
   - Implement transactions for multi-step operations

3. **GUI Layer** (PCPP 3.1–3.3):
   - Main window with proper layout
   - At least 5 different widget types
   - Use `grid()` layout manager
   - Event handlers for all interactions
   - Observable variables (`StringVar`, `IntVar`)
   - Input validation with user-friendly error messages

4. **Business Logic** (PCPP 1.4–1.6):
   - Service layer separating GUI from data access
   - Use decorators where appropriate
   - Static/class methods for utilities
   - Proper error handling

5. **Logging** (PCPP 5.2):
   - Configure logging with file and console handlers
   - Use appropriate log levels
   - Custom formatter with timestamp, level, message
   - Log important operations and errors

6. **Configuration** (PCPP 5.2):
   - Use `ConfigParser` to read settings from `.ini` file
   - Database path, log file path, application settings
   - Graceful handling of missing config file

### Optional Advanced Features

- CSV import/export functionality
- Search/filter capabilities
- Data validation decorators
- Custom exceptions with chaining
- Unit tests for core functionality

## Architecture

Follow MVC or similar pattern:

- **Model**: Database access layer
- **View**: GUI components
- **Controller/Service**: Business logic connecting model and view

## File Structure

```
capstone1_fullstack_gui/
├── README.md              # Project documentation
├── requirements.txt       # Python dependencies
├── config.ini            # Configuration file
├── main.py              # Application entry point
├── models/              # Data models
│   ├── __init__.py
│   └── domain.py        # Domain classes
├── database/            # Database layer
│   ├── __init__.py
│   ├── connection.py    # Database connection management
│   └── dao.py           # Data access objects
├── services/            # Business logic
│   ├── __init__.py
│   └── service.py       # Service layer
├── gui/                 # GUI layer
│   ├── __init__.py
│   ├── main_window.py   # Main window
│   └── widgets.py       # Custom widgets
├── utils/               # Utilities
│   ├── __init__.py
│   ├── logging_config.py
│   └── config.py        # Configuration management
├── tests/               # Unit tests
│   ├── __init__.py
│   └── test_models.py
└── docs/                # Additional documentation
```

## Acceptance Criteria

- [ ] Application launches and runs without errors
- [ ] All CRUD operations work correctly
- [ ] GUI is functional and user-friendly
- [ ] Database operations use transactions appropriately
- [ ] Logging writes to both file and console
- [ ] Configuration file is read correctly
- [ ] Code follows PEP 8, PEP 257, PEP 484
- [ ] Proper error handling throughout
- [ ] Code is well-organized and documented
- [ ] README includes installation and usage instructions

## Submission Requirements

1. **Source Code**: Complete, working application
2. **README.md**: 
   - Project description
   - Installation instructions
   - Usage guide
   - Architecture overview
   - Screenshots (optional)
3. **Documentation**: Docstrings for all public APIs
4. **Tests**: At least 5 unit tests
5. **Git History**: Meaningful commit history

## Evaluation Rubric

See `assessments/final_practical.md` for detailed rubric.

**Key Areas**:
- Functionality (25%)
- Architecture & Design (20%)
- OOP Implementation (15%)
- Code Quality (15%)
- Error Handling (10%)
- Testing (10%)
- Documentation (5%)

## Suggested Timeline

- **Week 1**: Design, database schema, basic models
- **Week 2**: GUI implementation, service layer
- **Week 3**: Integration, testing, documentation, polish

## Tips

- Start with a simple domain you understand well
- Build incrementally: database → models → services → GUI
- Test each layer independently
- Use logging from the start to debug issues
- Keep GUI and business logic separate
- Commit frequently with meaningful messages

Good luck!
