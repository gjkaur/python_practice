"""File persistence (PCAP 5.4-5.5)."""
import json
import errno
from pathlib import Path
from models import Expense

def load_expenses(path: str) -> list[Expense]:
    try:
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
        return [Expense.from_dict(d) for d in data]
    except OSError as e:
        if e.errno == errno.ENOENT:
            return []
        raise
    except json.JSONDecodeError:
        return []

def save_expenses(path: str, expenses: list[Expense]) -> None:
    Path(path).parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        json.dump([e.to_dict() for e in expenses], f, indent=2)
