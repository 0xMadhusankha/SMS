# 🎓 Student Management System (CLI)

A simple command-line based Student Management System built with Python.
This project allows users to manage student records with basic CRUD operations and JSON-based data persistence.

---

## 🚀 Features

* ➕ Add new students
* 📋 View all students
* 💾 Save student records to JSON file
* 📂 Load existing records on startup
* 🧱 Modular function-based design

---

## 🛠️ Tech Stack

* Python 3
* JSON (for data storage)
* CLI (Command Line Interface)
* UV (Python environment manager)

---

## 📁 Project Structure

```
SMS-project/
│── main.py
│── data/
│   └── students.json
```

---

## ▶️ How to Run

Make sure you have UV installed.

```bash
uv run python main.py
```

---

## 🧪 Usage

1. Run the program
2. Select options from the menu:

   * `1` → Add student
   * `2` → View students
   * `6` → Save records
   * `7` → Exit

---

## 💾 Data Storage

* Student records are stored in:

  ```
  data/students.json
  ```
* Data is saved in JSON format
* Automatically loaded when the program starts

---

## ⚠️ Current Limitations

* No input validation (e.g., age format)
* No search/update/delete functionality yet

---

## 🚀 Future Improvements

* 🔍 Search student by ID or name
* ✏️ Update student details
* ❌ Delete student records
* ✅ Input validation and error handling
* 🧠 Add logging

---

## 🧠 Learning Purpose

This project is built to practice:

* Python fundamentals
* File handling (JSON)
* CLI application design
* Git & GitHub workflow (branching, PRs)

---
