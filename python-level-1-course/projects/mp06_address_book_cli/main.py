"""
CLI entrypoint for the Address Book mini-project.
"""

from __future__ import annotations

from contacts import Contacts, add_or_update_contact, delete_contact, list_contacts, search_contacts
from formatting import format_contact_list


def _valid_email(email: str) -> bool:
    email = email.strip()
    if "@" not in email:
        return False
    local, _, domain = email.partition("@")
    return bool(local) and "." in domain


def print_menu() -> None:
    print("Address Book")
    print("------------")
    print("1) Add or update contact")
    print("2) Delete contact")
    print("3) Search contacts")
    print("4) List all contacts")
    print("0) Exit")


def main() -> None:
    contacts: Contacts = {}

    while True:
        print_menu()
        choice = input("Choose: ").strip()

        if choice == "1":
            name = input("Name : ").strip()
            if not name:
                print("Name cannot be empty.")
                continue
            phone = input("Phone: ").strip()
            email = input("Email: ").strip()
            if not _valid_email(email):
                print("Email does not look valid.")
                continue
            add_or_update_contact(contacts, name, phone, email)
            print("Contact saved.")

        elif choice == "2":
            name = input("Name to delete: ").strip()
            if delete_contact(contacts, name):
                print("Deleted.")
            else:
                print("Contact not found.")

        elif choice == "3":
            query = input("Search query: ")
            results = search_contacts(contacts, query)
            print(f"Found {len(results)} contact(s):")
            print(format_contact_list(results))

        elif choice == "4":
            print(format_contact_list(list_contacts(contacts)))

        elif choice == "0":
            break

        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()

