"""
In-memory contact management for the Address Book CLI.
"""

from __future__ import annotations

from typing import Dict, List, TypedDict


class Contact(TypedDict):
    name: str
    phone: str
    email: str


Contacts = Dict[str, Contact]


def _normalize_name(name: str) -> str:
    return name.strip().lower()


def add_or_update_contact(contacts: Contacts, name: str, phone: str, email: str) -> None:
    key = _normalize_name(name)
    contacts[key] = {"name": name.strip(), "phone": phone.strip(), "email": email.strip()}


def delete_contact(contacts: Contacts, name: str) -> bool:
    key = _normalize_name(name)
    if key in contacts:
        del contacts[key]
        return True
    return False


def search_contacts(contacts: Contacts, query: str) -> List[Contact]:
    norm_query = query.strip().lower()
    if not norm_query:
        return []
    return [c for c in contacts.values() if norm_query in c["name"].lower()]


def list_contacts(contacts: Contacts) -> List[Contact]:
    # Return contacts sorted by name for deterministic output.
    return sorted(contacts.values(), key=lambda c: c["name"].lower())

