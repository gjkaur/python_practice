"""
PCPP 5.1, 5.2: Database & File Processing Demo

Demonstrates:
- SQLite database operations
- CSV processing
- Logging configuration
- ConfigParser usage
"""

import configparser
import csv
import logging
import sqlite3
from contextlib import contextmanager
from typing import Iterator


# PCPP 5.1: SQLite Database
@contextmanager
def get_db_connection(db_path: str = ":memory:"):
    """Context manager for database connections."""
    conn = sqlite3.connect(db_path)
    try:
        yield conn
    finally:
        conn.close()


def create_database() -> None:
    """PCPP 5.1: Create database and tables."""
    with get_db_connection("example.db") as conn:
        cursor = conn.cursor()
        
        # Create table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                email TEXT UNIQUE NOT NULL,
                age INTEGER
            )
        """)
        
        conn.commit()
        print("Database and table created")


def crud_operations() -> None:
    """PCPP 5.1: Demonstrate CRUD operations."""
    with get_db_connection("example.db") as conn:
        cursor = conn.cursor()
        
        # INSERT
        cursor.execute(
            "INSERT INTO users (name, email, age) VALUES (?, ?, ?)",
            ("Alice", "alice@example.com", 30)
        )
        
        # INSERT many
        users = [
            ("Bob", "bob@example.com", 25),
            ("Charlie", "charlie@example.com", 35)
        ]
        cursor.executemany(
            "INSERT INTO users (name, email, age) VALUES (?, ?, ?)",
            users
        )
        
        conn.commit()
        
        # SELECT - PCPP 5.1: fetchone() and fetchall()
        cursor.execute("SELECT * FROM users WHERE name = ?", ("Alice",))
        one_row = cursor.fetchone()  # Single row or None
        print(f"fetchone() (Alice): {one_row}")
        cursor.execute("SELECT * FROM users")
        rows = cursor.fetchall()
        print("All users (fetchall()):")
        for row in rows:
            print(f"  {row}")
        
        # UPDATE
        cursor.execute(
            "UPDATE users SET age = ? WHERE name = ?",
            (31, "Alice")
        )
        conn.commit()
        
        # DELETE
        cursor.execute("DELETE FROM users WHERE name = ?", ("Charlie",))
        conn.commit()


# PCPP 5.2: CSV Processing
def csv_example() -> None:
    """PCPP 5.2: Read and write CSV files."""
    # Write CSV
    data = [
        {"name": "Alice", "age": 30, "city": "New York"},
        {"name": "Bob", "age": 25, "city": "London"},
        {"name": "Charlie", "age": 35, "city": "Tokyo"}
    ]
    
    with open("users.csv", "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["name", "age", "city"])
        writer.writeheader()
        writer.writerows(data)
    
    # Read CSV
    with open("users.csv", "r", newline="") as f:
        reader = csv.DictReader(f)
        print("\nCSV Data:")
        for row in reader:
            print(f"  {row['name']}, {row['age']}, {row['city']}")


# PCPP 5.2: Logging (LogRecord attributes in format)
def logging_example() -> None:
    """PCPP 5.2: Configure and use logging; format uses LogRecord attributes."""
    # Configure logging - format string uses LogRecord attributes: asctime, name, levelname, message
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler('app.log'),
            logging.StreamHandler()
        ]
    )
    
    logger = logging.getLogger(__name__)
    
    logger.debug("Debug message (not shown)")
    logger.info("Info message")
    logger.warning("Warning message")
    logger.error("Error message")


# PCPP 5.2: ConfigParser and interpolating values in .ini files
def configparser_example() -> None:
    """PCPP 5.2: Read and write configuration files; interpolating values in .ini."""
    # Create config
    config = configparser.ConfigParser()
    config['database'] = {
        'host': 'localhost',
        'port': '5432',
        'name': 'mydb'
    }
    config['app'] = {
        'debug': 'False',
        'log_level': 'INFO'
    }
    # Interpolation: reference other values with %(key)s (e.g. in a "url" option)
    config['paths'] = {
        'data': '/var/data',
        'report': '%(data)s/reports'  # Interpolates to /var/data/reports
    }

    # Write config
    with open('config.ini', 'w') as f:
        config.write(f)

    # Read config
    config_read = configparser.ConfigParser()
    config_read.read('config.ini')

    print("\nConfig values:")
    print(f"Database host: {config_read.get('database', 'host')}")
    print(f"App debug: {config_read.getboolean('app', 'debug')}")
    print(f"Interpolated path (paths.report): {config_read.get('paths', 'report')}")


if __name__ == "__main__":
    print("=== Database Operations ===")
    create_database()
    crud_operations()
    
    print("\n=== CSV Processing ===")
    csv_example()
    
    print("\n=== Logging ===")
    logging_example()
    
    print("\n=== ConfigParser ===")
    configparser_example()
