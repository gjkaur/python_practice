"""File I/O (PCAP 5.4-5.5)."""
import json
import errno
from pathlib import Path
from models import Item

def load_items(path: str) -> list[Item]:
    try:
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
        return [Item.from_dict(d) for d in data]
    except OSError as e:
        if e.errno == errno.ENOENT:
            return []
        raise
    except json.JSONDecodeError:
        return []

def save_items(path: str, items: list[Item]) -> None:
    Path(path).parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        json.dump([i.to_dict() for i in items], f, indent=2)
