"""
Core inventory operations for the Inventory Management CLI.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Dict


@dataclass
class Product:
    sku: str
    name: str
    price: float
    quantity: int


Inventory = Dict[str, Product]


def add_product(inventory: Inventory, sku: str, name: str, price: float, quantity: int) -> None:
    inventory[sku] = Product(sku=sku, name=name, price=price, quantity=quantity)


def adjust_quantity(inventory: Inventory, sku: str, delta: int) -> bool:
    product = inventory.get(sku)
    if product is None:
        return False
    new_quantity = product.quantity + delta
    if new_quantity < 0:
        return False
    product.quantity = new_quantity
    return True


def list_inventory(inventory: Inventory) -> Inventory:
    return dict(inventory)


def low_stock(inventory: Inventory, threshold: int) -> Inventory:
    return {sku: p for sku, p in inventory.items() if p.quantity < threshold}

