"""
PCPP All Sections: Integration Demo

Demonstrates integrating GUI, database, and networking in a complete application.
This is a simplified example showing the architecture pattern.
"""

import logging
import sqlite3
import tkinter as tk
from typing import Dict, List, Optional

import requests


# Architecture: MVC Pattern
# Model: Data layer
class DatabaseModel:
    """PCPP 5.1: Database model layer."""
    
    def __init__(self, db_path: str) -> None:
        """Initialize database model."""
        self.db_path = db_path
        self._init_database()
    
    def _init_database(self) -> None:
        """Initialize database schema."""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS items (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                value REAL
            )
        """)
        conn.commit()
        conn.close()
    
    def add_item(self, name: str, value: float) -> int:
        """Add item to database."""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO items (name, value) VALUES (?, ?)",
            (name, value)
        )
        item_id = cursor.lastrowid
        conn.commit()
        conn.close()
        return item_id
    
    def get_all_items(self) -> List[Dict[str, any]]:
        """Get all items from database."""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute("SELECT id, name, value FROM items")
        rows = cursor.fetchall()
        conn.close()
        return [{'id': r[0], 'name': r[1], 'value': r[2]} for r in rows]


# Service: Business logic layer
class ItemService:
    """Service layer for item operations."""
    
    def __init__(self, model: DatabaseModel) -> None:
        """Initialize service with model."""
        self.model = model
        self.logger = logging.getLogger(__name__)
    
    def create_item(self, name: str, value: float) -> Dict[str, any]:
        """Create new item with validation."""
        if not name or value < 0:
            raise ValueError("Invalid item data")
        
        item_id = self.model.add_item(name, value)
        self.logger.info(f"Created item: {name} (ID: {item_id})")
        return {'id': item_id, 'name': name, 'value': value}
    
    def list_items(self) -> List[Dict[str, any]]:
        """Get all items."""
        return self.model.get_all_items()


# View: GUI layer
class ItemView:
    """PCPP 3.2, 3.3: GUI view layer."""
    
    def __init__(self, service: ItemService) -> None:
        """Initialize view with service."""
        self.service = service
        self.root = tk.Tk()
        self.root.title("Item Manager")
        self._setup_ui()
    
    def _setup_ui(self) -> None:
        """Set up user interface."""
        # Entry fields
        tk.Label(self.root, text="Name:").grid(row=0, column=0, padx=5, pady=5)
        self.name_entry = tk.Entry(self.root, width=20)
        self.name_entry.grid(row=0, column=1, padx=5, pady=5)
        
        tk.Label(self.root, text="Value:").grid(row=1, column=0, padx=5, pady=5)
        self.value_entry = tk.Entry(self.root, width=20)
        self.value_entry.grid(row=1, column=1, padx=5, pady=5)
        
        # Buttons
        tk.Button(
            self.root,
            text="Add Item",
            command=self._on_add_clicked
        ).grid(row=2, column=0, columnspan=2, pady=10)
        
        tk.Button(
            self.root,
            text="Refresh List",
            command=self._on_refresh_clicked
        ).grid(row=3, column=0, columnspan=2, pady=5)
        
        # Listbox for items
        self.listbox = tk.Listbox(self.root, width=40, height=10)
        self.listbox.grid(row=4, column=0, columnspan=2, padx=5, pady=5)
    
    def _on_add_clicked(self) -> None:
        """Handle add button click."""
        try:
            name = self.name_entry.get()
            value = float(self.value_entry.get())
            self.service.create_item(name, value)
            self.name_entry.delete(0, tk.END)
            self.value_entry.delete(0, tk.END)
            self._on_refresh_clicked()
        except ValueError as e:
            tk.messagebox.showerror("Error", str(e))
    
    def _on_refresh_clicked(self) -> None:
        """Refresh item list."""
        self.listbox.delete(0, tk.END)
        items = self.service.list_items()
        for item in items:
            self.listbox.insert(
                tk.END,
                f"{item['name']}: ${item['value']:.2f}"
            )
    
    def run(self) -> None:
        """Start GUI event loop."""
        self.root.mainloop()


# Main application
def create_app() -> None:
    """Create and run integrated application."""
    # Configure logging (PCPP 5.2)
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s'
    )
    
    # Initialize layers
    model = DatabaseModel("items.db")
    service = ItemService(model)
    view = ItemView(service)
    
    # Run application
    view.run()


if __name__ == "__main__":
    create_app()
