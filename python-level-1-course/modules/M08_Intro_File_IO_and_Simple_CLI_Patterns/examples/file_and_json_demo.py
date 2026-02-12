"""
Example: Reading/writing text and JSON.
Run from repo root or ensure data/ exists.
"""
import json
from pathlib import Path

def read_text_file(path: str) -> str:
    with open(path, "r", encoding="utf-8") as f:
        return f.read()

def write_text_file(path: str, content: str) -> None:
    Path(path).parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)

def load_json_safe(path: str, default: dict = None):
    default = default or {}
    p = Path(path)
    if not p.exists():
        return default
    try:
        return json.loads(p.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return default

# Demo (writes to current directory if run)
# write_text_file("data/sample.txt", "Hello\\n")
# print(load_json_safe("data/config.json", {"key": "default"}))
