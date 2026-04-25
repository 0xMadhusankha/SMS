# 📋 Project Planner — Student Management System

---

## Project Name

Student Management System (CLI)

---

## Problem Statement

Many schools, tutors, and small training centers need a simple way to store and manage student information. Keeping student records manually can be slow and confusing, especially when searching, updating, or deleting student details. The problem is to create a basic Python command-line application that allows users to manage student records in an organized way.

---

## Objective

Build a Python command-line application that allows users to add, view, search, update, delete, and save student records. The application must validate all input, handle duplicate names using ID-based selection, and persist data between sessions using a JSON file.

---

## Features

- ➕ Add a new student with name, age, and grade validation
- 📋 View all students in the system
- 🔍 Search for students by name — partial, case-insensitive match
- ✏️ Update student details — press Enter to keep the current value
- ❌ Delete a student with confirmation before removal
- 💾 Save records to `data/students.json` — persists between sessions
- 🆔 ID-based selection to resolve duplicate names during update and delete
- ⚠️ Input validation — blocks empty input and enforces correct formats
- 🛡️ Exception handling — handles corrupted JSON file without crashing

---

## Functions

| Function | Purpose |
|----------|---------|
| `load_students()` | Loads saved student data from JSON file on startup. Returns empty list if file is missing or corrupted. |
| `save_record()` | Saves the current student list to `data/students.json`. Creates the `data/` folder if missing. |
| `get_valid_name()` | Validates name input. Blocks empty input and non-letter characters. Loops until valid. |
| `get_valid_age()` | Validates age input. Must be a whole number between 1 and 30. Returns value as `int`. |
| `get_valid_grade()` | Validates grade against the `ALLOWED_GRADES` constant. Case-insensitive. Loops until valid. |
| `find_student_by_name_then_id()` | Shared helper for update and delete. Searches by name, shows all matches, then prompts user to select by ID. |
| `add_student()` | Collects validated name, age, and grade. Generates a unique ID and appends the new record to the list. |
| `view_student()` | Loops through the student list and prints every record. Shows message if list is empty. |
| `search_student()` | Finds all students whose name contains the search term. Shows all matches with their IDs. |
| `update_student()` | Uses shared helper to find a student, then allows updating name, age, or grade. Empty input keeps current value. |
| `delete_student()` | Uses shared helper to find a student, asks for confirmation, then removes the record from the list. |
| `main()` | Runs the main menu loop. Loads data on start, shows menu, calls the matching function for each choice. |

---

## To-Do

- [x] Plan project — define features, structure, and data format
- [x] Create menu — build the `main()` function with `while` loop and options
- [x] Build features — implement all 6 core functions
- [x] Add input validation — name, age, and grade validators
- [x] Fix ID duplication bug — use highest ID + 1 instead of `len() + 1`
- [x] Fix age type bug — store age as `int`, not string
- [x] Fix delete label bug — correct `action_label` in delete flow
- [x] Add exception handling — handle corrupted JSON gracefully
- [x] Test program — manually test all 7 menu options
- [x] Fix bugs — identified and resolved via self PR review
- [x] Write documentation — `README.md` and `PROJECT_PLANNER.md`
- [x] Final review

---

## Progress Notes

### Phase 1 — Initial Build
- Built the basic CLI menu with 7 options
- Implemented all 6 core features: add, view, search, update, delete, save
- Used a Python list of dictionaries as the main data structure
- Added JSON file loading and saving with `os.makedirs()` for folder creation

### Phase 2 — Validation & Bug Fixes
- Added `get_valid_name()`, `get_valid_age()`, `get_valid_grade()` helper functions
- Added `find_student_by_name_then_id()` to handle duplicate name scenarios
- Opened a self-review Pull Request on GitHub to identify issues formally
- Identified and fixed 7 bugs through the PR review process

### Phase 3 — Documentation
- Wrote `README.md` covering problem statement, features, how to run, and functions
- Completed `PROJECT_PLANNER.md`
- Pushed final version to GitHub with clean commit history

---

## Problems and Fixes

| Problem | Fix Applied |
|---------|------------|
| ID duplication after delete — `len(students)+1` reuses IDs of deleted records | Find the highest existing ID and add 1 to it instead of using `len()` |
| Age stored as string — `input()` always returns text, causing type inconsistency in JSON | Return `int` from `get_valid_age()` and use `int(new_age)` in update flow |
| Wrong action label in delete — `"update"` was passed instead of `"delete"` | Changed argument to `find_student_by_name_then_id(students, "delete")` |
| No feedback on cancel — user got no message when typing `"no"` in delete confirm | Added `else: print("Delete cancelled.")` after the `if confirm == "yes"` block |
| Grade not validated — any text was accepted as a valid grade | Added `ALLOWED_GRADES` global constant and checked input against it |
| Duplicate grade list — `allowed_grades` defined inside two separate functions | Moved to a single `ALLOWED_GRADES` global constant used everywhere |
| Empty search matches all — empty string is found inside every string in Python | Block empty search input with a `while` loop before running the search |

---

## Future Improvements

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
- Allow searching by student ID in addition to name
