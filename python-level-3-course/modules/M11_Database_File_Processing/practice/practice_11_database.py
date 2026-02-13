"""
PCPP 5.1, 5.2: Practice Exercises - Database & File Processing
"""

import configparser
import csv
import logging
import sqlite3
from typing import Dict, List, Any


# Exercise 1: Database CRUD
# TODO: Create a database with a 'products' table:
#   - Columns: id (PRIMARY KEY), name, price, stock
#   - Implement functions: add_product(), get_product(), update_stock(), delete_product()
#   - Use parameterized queries

def create_products_table(conn: sqlite3.Connection) -> None:
    """Create products table."""
    # TODO: Implement
    pass


def add_product(conn: sqlite3.Connection, name: str, price: float, stock: int) -> int:
    """Add product and return product ID."""
    # TODO: Implement
    pass


def get_product(conn: sqlite3.Connection, product_id: int) -> Dict[str, Any] | None:
    """Get product by ID."""
    # TODO: Implement
    pass


# Exercise 2: Transactions
# TODO: Implement a function that:
#   - Updates multiple products in a transaction
#   - Rolls back if any update fails
#   - Uses context manager for connection

def update_multiple_products(updates: List[Dict[str, Any]]) -> None:
    """Update multiple products in a transaction."""
    # TODO: Implement
    pass


# Exercise 3: CSV Import/Export
# TODO: Create functions to:
#   - Export products from database to CSV
#   - Import products from CSV to database
#   - Handle errors gracefully

def export_to_csv(conn: sqlite3.Connection, filename: str) -> None:
    """Export products to CSV file."""
    # TODO: Implement
    pass


def import_from_csv(conn: sqlite3.Connection, filename: str) -> None:
    """Import products from CSV file."""
    # TODO: Implement
    pass


# Exercise 4: Logging Configuration
# TODO: Set up logging with:
#   - File handler and console handler
#   - Custom format with timestamp, level, message
#   - Different log levels for different modules

def setup_logging() -> None:
    """Configure logging system."""
    # TODO: Implement
    pass


# Exercise 5: ConfigParser
# TODO: Create a configuration system:
#   - Read database settings from config.ini
#   - Read application settings
#   - Use interpolation for values

def load_config(filename: str) -> configparser.ConfigParser:
    """Load configuration from INI file."""
    # TODO: Implement
    pass


if __name__ == "__main__":
    print("Complete the exercises above!")
