# 🎓 Student Management System (CLI)

A simple command-line based Student Management System built with Python.
This application allows managing student records with full CRUD operations and JSON-based data persistence.

---

## 🚀 Features

* ➕ Add new students
* 📋 View all students
* 🔍 Search students (case-insensitive, partial match)
* ✏️ Update student details
* ❌ Delete student records
* 🆔 Handle duplicate names using ID selection
* 💾 Save records to JSON file
* 📂 Load records automatically on startup
* ⚠️ Basic input validation and error handling
* 🧱 Modular function-based design

---

## 🛠️ Tech Stack

* Python 3
* JSON (data storage)
* CLI (Command Line Interface)
* UV (Python environment manager)

---

## 📁 Project Structure

```id="proj-struct"
SMS-project/
│── main.py
│── data/
│   └── students.json
```

---

## ▶️ How to Run

```bash id="run-cmd"
uv run python main.py
```

---

## 🧪 Usage

1. Run the program
2. Select options from the menu:

   * `1` → Add student
   * `2` → View all students
   * `3` → Search student
   * `4` → Update student
   * `5` → Delete student
   * `6` → Save records
   * `7` → Exit

---

## 💾 Data Storage

* Student records are stored in:

  ```id="json-path"
  data/students.json
  ```

* Data is saved in JSON format

* Automatically loaded on startup

* Handles corrupted files by falling back to an empty list

---

## ⚠️ Current Limitations

* No user authentication (no login system)
* No role-based access control (anyone can modify data)
* Data is stored in plain JSON (not secure)
* No database support (scalability limitations)
* Single-user CLI only

---

## 🚀 Future Improvements

### 🔐 Security & Access Control

* Add login system with password hashing (SHA-256)
* Implement Role-Based Access Control (Admin / User)
* Restrict delete/update operations to authorized users

### 🗄️ Database Migration

* Replace JSON storage with SQLite database
* Improve data integrity and query performance
* Support scalable data handling

### ⚙️ System Enhancements

* Add logging system
* Improve validation and error handling
* Add automated testing

---

## 🧠 Learning Purpose

This project demonstrates:

* Python fundamentals
* File handling (JSON)
* CLI application design
* Data validation and consistency
* Debugging and code refactoring
* Git & GitHub workflow (branching, PR reviews, bug fixing)

---
