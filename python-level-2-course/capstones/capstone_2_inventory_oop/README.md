# Capstone 2 – Inventory / Order System (OOP + Modules + Exceptions)

## Overview

CLI **Inventory** system with **multiple modules**, **OOP** (Item, Inventory classes), **custom exceptions**, and **file I/O**. Aligns with PCAP: modules, exceptions, OOP, I/O.

## Requirements

- **Models**: Item (id, name, quantity, price) or similar; Inventory holds items and provides add/update/list.
- **Exceptions**: ValidationError, DuplicateError, NotFoundError for business rules.
- **Storage**: JSON persistence; handle missing file (errno).
- **CLI**: add item, update quantity, list items, exit.

## Milestones

- **MVP**: Add item, list, save/load.
- **v2**: Update quantity; validate positive quantity.
- **v3**: Search by name; summary total value.

## Suggested Structure

- main.py, models.py, services.py, storage.py, validators.py, exceptions.py
- data/ for JSON
