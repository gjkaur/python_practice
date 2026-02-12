"""CLI: save and load text file; handle missing file."""
from storage import save_text, load_text

def main():
    path = input("File path: ").strip() or "demo_save.txt"
    content = input("Content to save: ").strip() or "default content"
    save_text(path, content)
    print("Saved.")
    loaded = load_text(path)
    print("Loaded:", loaded)
    missing = load_text("nonexistent_xyz_123.txt")
    print("Load missing file:", missing)

if __name__ == "__main__":
    main()
