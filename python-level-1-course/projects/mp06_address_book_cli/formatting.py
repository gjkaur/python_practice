"""
Formatting helpers for Address Book CLI output.
"""

from __future__ import annotations

from typing import Iterable

from contacts import Contact


def format_contact(contact: Contact) -> str:
    return f"{contact['name']} | {contact['phone']} | {contact['email']}"


def format_contact_list(contacts: Iterable[Contact]) -> str:
    lines = [format_contact(c) for c in contacts]
    return "\n".join(lines) if lines else "No contacts found."

