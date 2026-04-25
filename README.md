# 🎓 Student Management System (CLI)

A simple command-line based Student Management System built with Python. This application allows managing student records with full CRUD operations and JSON-based data persistence.

---

## 🚀 Features

- ➕ Add new students with validated input
- 📋 View all students
- 🔍 Search students (case-insensitive, partial match)
- ✏️ Update student details
- ❌ Delete student records with confirmation
- 🆔 Handle duplicate names using ID-based selection
- 💾 Save records to JSON file
- 📂 Load records automatically on startup
- ⚠️ Input validation for name, age, and grade
- 🛡️ Graceful handling of corrupted JSON files
- 🧱 Modular function-based design

---

## 🛠️ Tech Stack

- Python 3
- JSON (data storage)
- CLI (Command Line Interface)
- UV (Python environment manager)

---

## 📁 Project Structure

```
SMS-project/
├── main.py
├── README.md
├── .gitignore
└── data/
    └── students.json
```

---

## ▶️ How to Run

**1. Clone the repository**

```bash
git clone https://github.com/0xMadhusankha/SMS.git
cd SMS-project
```

**2. Run the application**

```bash
uv run python main.py
```

---

## 🧪 Usage

Run the program and select options from the menu:

```
=== Student Management System ===

1. Add student
2. View All students
3. Search student
4. Update student
5. Delete student
6. Save records
7. Exit
```

| Option | Action |
|--------|--------|
| `1` | Add a new student |
| `2` | View all students |
| `3` | Search by name |
| `4` | Update student details |
| `5` | Delete a student |
| `6` | Save records to file |
| `7` | Save and exit |

---

## 🔍 How Search, Update, and Delete Work

These three operations all use the same smart name-matching flow:

1. Enter a name to search (partial match supported)
2. All matching records are displayed with their IDs
3. If only one match — you are asked to confirm
4. If multiple matches — you pick the exact student by ID

This prevents accidentally modifying the wrong record when two students share the same name.

---

## ✅ Input Validation Rules

| Field | Rule |
|-------|------|
| Name  | Letters only, cannot be empty |
| Age   | Whole number, must be between 1 and 30 |
| Grade | Must be one of: `A+` `A` `A-` `B+` `B` `B-` `C+` `C` `C-` `D+` `D` `D-` `F` |

---

## 💾 Data Storage

Student records are stored in:

```
data/students.json
```

- Data is saved in JSON format
- Automatically loaded on startup
- Auto-saved when exiting via option `7`
- Handles corrupted files gracefully by falling back to an empty list

---

## ⚙️ Functions Overview

| Function | Purpose |
|----------|---------|
| `load_students()` | Loads saved data from JSON on startup |
| `save_record()` | Writes current student list to JSON file |
| `get_valid_name()` | Validates name — blocks empty and non-letter input |
| `get_valid_age()` | Validates age — must be a number between 1 and 30 |
| `get_valid_grade()` | Validates grade against the allowed grades list |
| `find_student_by_name_then_id()` | Shared helper — searches by name then selects by ID |
| `add_student()` | Collects input and appends a new student record |
| `view_student()` | Displays all student records |
| `search_student()` | Finds and displays students matching a name search |
| `update_student()` | Updates name, age, or grade of a selected student |
| `delete_student()` | Removes a selected student after confirmation |
| `main()` | Runs the main menu loop |

---

## ⚠️ Current Limitations

- No user authentication (no login system)
- No role-based access control (anyone can modify data)
- Data is stored in plain JSON (not encrypted)
- No database support (scalability limitations)
- Single-user CLI only

---

## 🚀 Future Improvements

### 🔐 Security & Access Control
- Add login system with password hashing (SHA-256)
- Implement Role-Based Access Control (Admin / User)
- Restrict delete and update operations to authorized users

### 🗄️ Database Migration
- Replace JSON storage with SQLite database
- Improve data integrity and query performance
- Support scalable data handling

### ⚙️ System Enhancements
- Add sorting — sort view output by name, age, or grade
- Export to CSV — allow exporting student records
- Add logging system
- Add automated unit testing using Python's `unittest` module

---

## 🧠 Learning Purpose

This project demonstrates:

- Python fundamentals (variables, lists, dictionaries, functions, loops)
- File handling (JSON read/write)
- CLI application design
- Input validation and data consistency
- Exception handling
- Debugging and code refactoring
- Git & GitHub workflow (branching, PR reviews, self-review, bug fixing)
