## MP06 – Address Book CLI

### 1. Problem Statement

You are building a simple, in-memory **address book**.  
Users should be able to:

- Add a contact (name, phone, email).
- Update a contact.
- Delete a contact.
- Search for contacts by name (partial match).

This project reinforces dictionaries, strings, and simple CLI patterns.

---

### 2. User Stories

- **As a user**, I want to manage a small set of contacts from the command line.
- **As a developer**, I want contact storage to be clearly modeled and easy to extend.
- **As a maintainer**, I want search to be case-insensitive and robust against whitespace issues.

---

### 3. Inputs and Outputs

**Inputs**

- Contact name (string).
- Phone number (string; no strict validation yet).
- Email address (string; basic validation only).
- Menu choices:
  - `1` – Add or update contact.
  - `2` – Delete contact.
  - `3` – Search contacts.
  - `4` – List all contacts.
  - `0` – Exit.

**Outputs**

- Confirmation for add/update/delete.
- Search results (possibly empty).
- Full listing of contacts with consistent formatting.

---

### 4. Constraints and Validation Rules

- Names must be non-empty after trimming.
- Use **case-insensitive keys** for storage (e.g., lowercased names).
- Basic email validation:
  - Must contain `@` and a dot `.` after `@` (simple check is fine).
- No crashes on invalid menu choices or blank input.

---

### 5. Suggested Architecture

```text
mp06_address_book_cli/
  main.py        # CLI handling and menu
  contacts.py    # CRUD operations and search
  formatting.py  # display helpers
  README.md
```

Responsibilities:

- `contacts.py`
  - Store data in a dict `{normalized_name: {"name": ..., "phone": ..., "email": ...}}`.
  - Functions:
    - `add_or_update_contact(name, phone, email)`
    - `delete_contact(name)`
    - `search_contacts(query) -> list[dict]`
    - `list_contacts() -> list[dict]`
- `formatting.py`
  - Helpers to format a single contact or a list into strings.
- `main.py`
  - Menu, prompts, and calling into `contacts.py`.

---

### 6. CLI Usage Examples

```bash
python main.py
```

Example interaction:

```text
1) Add or update contact
2) Delete contact
3) Search contacts
4) List all contacts
0) Exit

Choose: 1
Name : Alice Smith
Phone: 123-456-7890
Email: alice@example.com
Contact saved.

Choose: 3
Search query: alice
Found 1 contact(s):
- Alice Smith | 123-456-7890 | alice@example.com
```

---

### 7. Test Cases (At Least 8)

1. **Add contact** – new entry stored with normalized key.
2. **Update contact** – re-adding same name updates details, does not create duplicate.
3. **Delete contact** – entry removed; subsequent search/list confirms.
4. **Search by partial name** – returns all matches ignoring case and leading/trailing spaces.
5. **List all contacts** – prints consistent ordering (e.g., sorted by name).
6. **Invalid menu choice** – message + re-prompt, no crash.
7. **Invalid email format** – simple validation fails with clear message (optional re-prompt).
8. **Empty address book** – search and list operations handle empty state gracefully.

---

### 8. Level-Up Extensions

- Add **categories/tags** for each contact (e.g., family, work).
- Persist contacts to JSON between runs using a simple storage module.
- Add a **“favorite”** flag and list favorites separately.
- Implement a simple **import/export** from CSV.

