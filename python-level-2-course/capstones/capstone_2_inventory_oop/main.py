"""CLI entrypoint (Level 2 capstone 2)."""
from storage import load_items, save_items
from models import Item
from validators import validate_quantity
from services import find_by_id, update_quantity
from exceptions import ValidationError, NotFoundError

DATA_PATH = "data/inventory.json"

def main():
    items = load_items(DATA_PATH)
    while True:
        print("1) Add 2) List 3) Update qty 0) Exit")
        choice = input("Choice: ").strip()
        if choice == "0":
            save_items(DATA_PATH, items)
            break
        if choice == "1":
            try:
                iid = input("Id: ").strip()
                name = input("Name: ").strip()
                qty = validate_quantity(input("Quantity: "))
                price = float(input("Price: "))
                items.append(Item(iid, name, qty, price))
                print("Added.")
            except (ValidationError, ValueError) as e:
                print("Error:", e)
        elif choice == "2":
            for i in items:
                print(i)
        elif choice == "3":
            try:
                iid = input("Item id: ").strip()
                qty = validate_quantity(input("New quantity: "))
                update_quantity(items, iid, qty)
                print("Updated.")
            except (ValidationError, NotFoundError) as e:
                print("Error:", e)
        else:
            print("Unknown option")

if __name__ == "__main__":
    main()
