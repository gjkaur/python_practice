# MP10 – Database-Backed Application

**PCPP Objectives**: 5.1, 5.2  
**Week**: 11  
**Related Modules**: M11

## Goal

Build an application with SQLite database, file processing, and logging.

## Requirements

Create a database-backed application (choose domain: library, inventory, contacts, etc.):

- At least 2 related tables with foreign key relationships
- Implement full CRUD operations for both tables
- Use parameterized queries to prevent SQL injection
- Implement transactions for multi-step operations
- File processing:
  - Import data from CSV file into database
  - Export data from database to CSV file
  - Use `csv.DictReader` and `csv.DictWriter`
- Logging:
  - Set up logging with at least 2 handlers (file and console)
  - Use different log levels: `INFO` for operations, `ERROR` for failures
  - Custom formatter with timestamp, level, and message
- Configuration:
  - Use `ConfigParser` to read database path, log file path, and other settings from `.ini` file
  - Application reads config on startup

## Acceptance Criteria

- Database operations work correctly (create, read, update, delete)
- Foreign key relationships enforced (or handled gracefully)
- CSV import/export works without data loss
- Logging writes to both file and console with appropriate levels
- Configuration file is read correctly, application fails gracefully if missing
- Code uses proper error handling for database and file operations

## File Structure

```
mp10_database_app/
├── README.md
├── main.py            # Application entry point
├── database.py         # Database operations
├── models.py           # Data models
├── csv_handler.py      # CSV import/export
├── config.py           # Configuration management
├── logging_config.py   # Logging setup
├── config.ini          # Configuration file
└── tests/              # Unit tests
```

## Suggested Extensions

- Add database migration system (simple version tracking)
- Implement search/filter functionality with SQL `LIKE` or full-text search
- Add logging rotation (using `RotatingFileHandler`)
- Create a simple CLI interface for the application
- Add data validation before database insertion

## Submission Checklist

- [ ] Database with 2+ related tables
- [ ] CRUD operations implemented
- [ ] CSV import/export works
- [ ] Logging configured
- [ ] Configuration management works
- [ ] Error handling comprehensive
