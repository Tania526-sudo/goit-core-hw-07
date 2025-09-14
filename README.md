# CLI Assistant (Address Book)

A command-line assistant to manage an address book: contacts, phone numbers, and birthdays.  
Built with OOP (Field / Name / Phone / Birthday / Record / AddressBook), input validation, and
decorator-based error handling. Includes an upcoming birthdays helper that shifts weekend
birthdays to the next working day (Monday).

> Python ≥ 3.9 · Tests: `pytest` (optional) · Style: `ruff` + `black`

---

## Table of Contents
- [Features](#features)
- [Commands](#commands)
- [Installation](#installation)
- [How to Run](#how-to-run)
- [Quick Demo](#quick-demo)
- [Project Structure](#project-structure)
- [Class Overview](#class-overview)
- [Validation Rules](#validation-rules)
- [Error Handling](#error-handling)
- [Testing (optional)](#testing-optional)
- [Topics / Tags](#topics--tags)
- [License](#license)

---

## Features
- Address book stored as `AddressBook` (dict-like, based on `UserDict`)
- Records with `Name` (required), a list of `Phone` numbers, and optional `Birthday`
- Add / remove / edit / find phones per contact
- Add & show birthdays (format `DD.MM.YYYY`)
- Upcoming birthdays for the next 7 days (weekends shift to Monday)
- Friendly error messages via an `input_error` decorator
- Human-friendly printing for both `Record` and `AddressBook`
---

## Installation
```bash
git clone https://github.com/<your-username>/goit-core-hw-07.git
cd goit-core-hw-07

python -m venv .venv
# Windows:
.venv\Scripts\activate
# macOS / Linux:
source .venv/bin/activate

# Install dev tools (optional but recommended)
pip install -e ".[dev]"

---
#Project Structure
```bash
goit-core-hw-07/
├── README.md
├── pyproject.toml
├── src/
│   ├── address_book.py      # OOP models & logic
│   └── bot.py               # CLI bot using AddressBook
└── examples/
    └── demo.py              # Optional short demo (non-CLI)