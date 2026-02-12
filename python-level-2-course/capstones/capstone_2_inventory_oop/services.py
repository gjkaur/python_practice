"""Business logic (PCAP 4.x)."""
from models import Item
from exceptions import NotFoundError

def find_by_id(items: list[Item], item_id: str) -> Item | None:
    for i in items:
        if i.id == item_id:
            return i
    return None

def update_quantity(items: list[Item], item_id: str, quantity: int) -> None:
    item = find_by_id(items, item_id)
    if item is None:
        raise NotFoundError(f"Item {item_id} not found")
    item.quantity = quantity
