# Module 11 – Database & File Processing

**PCPP Objectives**: 5.1, 5.2

## Learning Objectives

- Connect to SQLite databases and perform CRUD operations
- Use transactions for data integrity
- Process CSV files using `csv` module
- Configure and use `logging` module
- Parse and create configuration files with `ConfigParser`
- Process XML files for data extraction

## Topics Covered

### Lesson 11.1 – SQLite Database Basics
- `sqlite3` module
- Creating connections and cursors
- Creating tables
- Basic SQL: SELECT, INSERT, UPDATE, DELETE

### Lesson 11.2 – CRUD Operations and Transactions
- Parameterized queries
- Cursor methods: `execute()`, `executemany()`, `fetchone()`, `fetchall()`
- Transactions: `commit()`, `rollback()`
- Context managers

### Lesson 11.3 – Advanced SQLite
- Foreign keys and joins
- Aggregations
- Constraints

### Lesson 11.4 – CSV and XML File Processing
- CSV: `csv.reader()`, `csv.writer()`, `csv.DictReader()`, `csv.DictWriter()`
- XML files: parsing with `ElementTree.parse()`, searching with `find()` and `findall()`, building with `Element` and `SubElement()` (same API as in M10; use with file paths)
- Handling CSV and XML files

### Lesson 11.5 – Logging Module
- Logging levels
- Basic configuration
- Formatting log messages using LogRecord attributes (e.g. `%(asctime)s`, `%(levelname)s`, `%(message)s`)

### Lesson 11.6 – Custom Handlers and Formatters
- File handlers
- Rotating file handlers
- Custom formatters (using LogRecord attributes)

### Lesson 11.7 – ConfigParser Module
- INI file format
- Reading and writing config files
- Interpolating values in .ini files (e.g. `%(key)s` in values to reference other options)

## Key Concepts

- **SQLite**: Embedded database for Python applications
- **Transactions**: Ensuring data consistency
- **CSV**: Comma-separated values for data exchange
- **Logging**: Professional error and event tracking
- **ConfigParser**: Configuration file management

## Practice Exercises

See `practice/practice_11_database.py`

## Examples

See `examples/database_demo.py`

## Related Mini Project

**MP10 – Database-Backed Application** (Week 11)

## Next Module

**M12 – Integration & Capstones** (All sections)
