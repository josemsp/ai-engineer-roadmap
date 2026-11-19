# AI Engineer Roadmap

My self-taught learning path to becoming an **AI Engineer**. This repository tracks progress week by week, along with the exercises and code modules I build throughout the course.

## Current Status

| Week | Topic | Status |
| ---- | ----- | ---------- |
| Week 1 | Python Fundamentals | 🟢 In progress |
| Weeks 2+ | To be defined | ⚪ Pending |

- **Course name:** AI Engineer Roadmap
- **Developer:** Manuel
- **Overall progress:** in progress

## Repository Structure

```
.
├── week-01/                     # Week 1 — Python Fundamentals
│   ├── .venv/                   # Virtual environment (ignored by Git)
│   └── src/
│       ├── main.py              # Base course welcome script
│       ├── day-1/               # Day 1 — Variables, data types and functions
│       │   ├── main.py
│       │   └── crud.py
│       ├── day-2/               # Day 2 — Conditionals, loops and modules
│       │   ├── main.py
│       │   ├── exercise.py
│       │   └── sys_users.py
│       └── day-3/               # Day 3 — Functions, type hints and user service
│           ├── main.py
│           └── user_service.py
└── .gitignore
```

## Contents

### Week 1 — Python Fundamentals

- **Day 1 — Variables and data types**
  - Variables and constants.
  - Lists, tuples, sets and dictionaries.
  - Set operations (intersection, union, unique values).
  - Functions and return values.
  - `crud.py`: basic create, read, update and delete operations on an in-memory user list.

- **Day 2 — Conditionals, loops and modules**
  - `if` / `elif` / `else`, logical operators.
  - `for` and `while` loops, using `range()`.
  - Importing local modules (`sys_users.py`).
  - `exercise.py`: user filtering, lookup by name, metrics and data validation.

- **Day 3 — Functions and user service**
  - Default parameters, variable arguments (`*args`) and type hints.
  - `user_service.py`: typed module to create, find, filter and deactivate users.
  - Exercises on prices, averages and user summaries.

## Requirements

- **Python 3.9 or higher** (type annotations such as `list[User]` are used).

No external dependencies: all code uses only the Python standard library.

## How to Run

Each week has its own virtual environment. From the corresponding week folder:

```bash
# 1. Create the virtual environment (only the first time)
python -m venv .venv

# 2. Activate the virtual environment
# Windows (PowerShell):
.venv\Scripts\Activate.ps1
# macOS / Linux:
source .venv/bin/activate

# 3. Run the desired script
python src/day-3/main.py
```

> **Note:** Scripts in `day-2` and `day-3` import local modules (`sys_users`, `user_service`), so they must be run from inside their own folder (or with that folder on the `PYTHONPATH`). For example:

```bash
cd week-01/src/day-3
python main.py
```

## Conventions

- Each week lives in its own `week-XX/` folder.
- Each day has a `day-X/` folder with its own `main.py` and supporting modules.
- Virtual environments (`.venv/`) and Python cache (`__pycache__/`) are excluded from the repository via `.gitignore`.
- Code is written in English (variable names, functions and docstrings); documentation is also in English.

## License

For personal learning use only.
