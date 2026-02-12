"""Practice: File I/O (PCAP 5.4-5.5).

Implement the functions. Run main() to test (creates/removes a temp file).
"""
import errno
import os


def write_one_line(path: str, content: str) -> None:
    """Open path for writing (text, utf-8), write content, close. Create parent dirs if needed."""
    os.makedirs(os.path.dirname(path) or ".", exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)


def read_entire_file(path: str) -> str | None:
    """Read and return entire file content as string. If file not found (ENOENT), return None. Re-raise other OSErrors."""
    try:
        with open(path, "r", encoding="utf-8") as f:
            return f.read()
    except OSError as e:
        if e.errno == errno.ENOENT:
            return None
        raise


def main() -> None:
    test_path = "tmp_practice_08.txt"
    write_one_line(test_path, "Hello from practice 08")
    print("Read back:", read_entire_file(test_path))
    print("Missing file:", read_entire_file("nonexistent_xyz_123.txt"))
    if os.path.exists(test_path):
        os.remove(test_path)


if __name__ == "__main__":
    main()
