"""File persistence (PCAP 5.4-5.5)."""
import errno

def save_text(path: str, content: str) -> None:
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)

def load_text(path: str) -> str | None:
    try:
        with open(path, "r", encoding="utf-8") as f:
            return f.read()
    except OSError as e:
        if e.errno == errno.ENOENT:
            return None
        raise
