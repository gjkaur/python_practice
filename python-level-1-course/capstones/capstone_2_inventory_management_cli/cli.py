"""
CLI entrypoint for the Inventory Management capstone.
"""

from __future__ import annotations

from inventory import Inventory, add_product, adjust_quantity, list_inventory, low_stock
from storage import load_inventory, save_inventory
from validators import read_float_positive, read_int, read_non_empty

LOW_STOCK_THRESHOLD = 5


def print_menu() -> None:
    print("Inventory Management")
    print("--------------------")
    print("1) Add product")
    print("2) Adjust quantity")
    print("3) List inventory")
    print("4) Show low-stock report")
    print("0) Exit")


def print_inventory(inventory: Inventory) -> None:
    if not inventory:
        print("No products in inventory.")
        return
    for sku, p in inventory.items():
        print(f"{sku} | {p.name} | {p.price:.2f} | qty={p.quantity}")


def main() -> None:
    inventory = load_inventory()

    while True:
        print_menu()
        choice = input("Choose: ").strip()

        if choice == "1":
            sku = read_non_empty("SKU: ")
            name = read_non_empty("Name: ")
            price = read_float_positive("Price: ")
            quantity = read_int("Initial quantity: ")
            if quantity < 0:
                print("Quantity cannot be negative.")
                continue
            add_product(inventory, sku=sku, name=name, price=price, quantity=quantity)
            save_inventory(inventory)
            print("Product added.")

        elif choice == "2":
            sku = read_non_empty("SKU: ")
            delta = read_int("Quantity change (positive for restock, negative for sale): ")
            if not adjust_quantity(inventory, sku=sku, delta=delta):
                print("Failed to adjust quantity (unknown SKU or invalid quantity).")
            else:
                save_inventory(inventory)
                print("Quantity updated.")

        elif choice == "3":
            print_inventory(list_inventory(inventory))

        elif choice == "4":
            ls = low_stock(inventory, threshold=LOW_STOCK_THRESHOLD)
            print(f"Products below threshold ({LOW_STOCK_THRESHOLD}):")
            print_inventory(ls)

        elif choice == "0":
            break

        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()

