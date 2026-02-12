"""
JSON-based storage for inventory.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Dict

from inventory import Inventory, Product

DATA_PATH = Path("data/inventory.json")


def load_inventory() -> Inventory:
    if not DATA_PATH.exists():
        return {}
    try:
        text = DATA_PATH.read_text(encoding="utf-8")
        raw = json.loads(text)
    except (OSError, json.JSONDecodeError):
        print("Warning: failed to load inventory; starting empty.")
        return {}

    inv: Inventory = {}
    if isinstance(raw, dict):
        for sku, info in raw.items():
            try:
                inv[sku] = Product(
                    sku=sku,
                    name=str(info["name"]),
                    price=float(info["price"]),
                    quantity=int(info["quantity"]),
                )
            except (KeyError, TypeError, ValueError):
                continue
    return inv


def save_inventory(inventory: Inventory) -> None:
    DATA_PATH.parent.mkdir(parents=True, exist_ok=True)
    raw: Dict[str, dict] = {}
    for sku, product in inventory.items():
        raw[sku] = {
            "name": product.name,
            "price": product.price,
            "quantity": product.quantity,
        }
    DATA_PATH.write_text(json.dumps(raw, indent=2), encoding="utf-8")

