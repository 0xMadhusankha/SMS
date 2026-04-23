import json
import os

DATA_FILE = "data/students.json"

#  GLOBAL CONSTANT
#  PR Review Fix #5 — allowed_grades was copy-pasted in two places
#  (get_valid_grade and update_student). If someone adds a new grade
#  later, they had to update two places and would likely miss one.
#  Moving it here means there is only ONE place to ever change it.


ALLOWED_GRADES = ["A+", "A", "A-", "B+", "B", "B-", "C+", "C", "C-", "D+", "D", "D-", "F"]

#  LOAD & SAVE

def load_students():
    # check if the data file exists before trying to open it
    if os.path.exists(DATA_FILE):
        try:
            # try to open and read the JSON file normally
            with open(DATA_FILE, "r") as file:
                return json.load(file)          # converts JSON text → Python list

        except json.JSONDecodeError:
            # PR Review Fix — this runs when the file exists but its content
            # is broken. Example: someone manually edited students.json
            # and made a formatting mistake. Without this, the whole program crashes.
            print("Warning: students.json is corrupted and could not be read.")
            print("Starting with an empty student list.")
            return []

        except Exception as error:
            # catches ANY other unexpected error — disk failure, permission denied, etc.
            print(f"Unexpected error while loading file: {error}")
            print("Starting with an empty student list.")
            return []

    return []   # file does not exist yet — this is a fresh start


def save_record(students):
    os.makedirs("data", exist_ok=True)      # create the data/ folder if it is missing
    with open(DATA_FILE, "w") as file:
        json.dump(students, file, indent=4) # converts Python list → JSON text and writes it
    print("Records saved successfully.")


#  INPUT VALIDATION HELPERS
#  These functions keep asking the user until the input is valid.
#  They are used by add_student().
#  For update_student() we validate differently — see note there.

def get_valid_name(prompt):
    # keeps looping until the user types a proper name
    while True:
        name = input(prompt).strip()    # .strip() removes extra spaces from start/end

        if name == "":
            print("Name cannot be empty. Please try again.")
            continue                    # go back to the top of the while loop

        # .replace(" ", "") removes spaces so "Ali Ahmed" doesn't fail the letter check
        # .isalpha() returns True only if every character is a letter
        if not name.replace(" ", "").isalpha():
            print("Name should only contain letters. Please try again.")
            continue

        return name     # name passed all checks — return it


def get_valid_age(prompt):
    # keeps looping until the user types a valid number age
    while True:
        age = input(prompt).strip()

        if age == "":
            print("Age cannot be empty. Please try again.")
            continue

        # .isdigit() returns True only if every character is a digit (0-9)
        # this blocks inputs like "abc", "20.5", "-5"
        if not age.isdigit():
            print("Age must be a number (e.g. 20). Please try again.")
            continue

        age_number = int(age)   # safe to convert now — we know it is all digits

        # PR Review Fix #7 — range was "< 1 or > 30" but message said "(1 - 30)"
        # condition and message must always match. Fixed both to 1-30.
        if age_number < 1 or age_number > 30:
            print("Please enter a realistic age (1 - 30).")
            continue

        return age_number   # return as int (not string) — age is a number, not text


def get_valid_grade(prompt):
    # keeps looping until the user types a grade from the allowed list
    while True:
        grade = input(prompt).strip().upper()   # .upper() so "a" → "A", "b+" → "B+"

        if grade == "":
            print("Grade cannot be empty. Please try again.")
            continue

        # PR Review Fix #5 — now uses the global ALLOWED_GRADES constant
        # instead of a local copy defined only inside this function
        if grade not in ALLOWED_GRADES:
            print(f"Invalid grade. Allowed grades: {', '.join(ALLOWED_GRADES)}")
            continue

        return grade    # grade is valid — return it


#  SHARED HELPER — find a student by name, then let user pick by ID
#
#  WHY this function exists:
#  If we just search by name and two students are both named "Ali",
#  we do not know which one the user means. This function:
#    1. Searches by name and shows ALL matches with their IDs
#    2. If only 1 match — asks the user to confirm
#    3. If multiple matches — asks the user to pick by ID
#
#  It is shared by update_student() and delete_student()
#  so the logic is written only once.
#
#  action_label is a word like "update" or "delete" — it is used
#  inside prompts so the message makes sense for each situation.


def find_student_by_name_then_id(students, action_label):

    # step 1 — ask for a name, block empty input
    while True:
        name = input("Enter name to search: ").strip().lower()
        if name == "":
            print("Search name cannot be empty. Please try again.")
        else:
            break   # valid input — exit the while loop

    # step 2 — find all students whose name contains what was typed
    matches = []                                # empty list to store found students
    for student in students:
        if name in student["name"].lower():     # case-insensitive partial match
            matches.append(student)             # add matched student to list

    # step 3 — if nothing found, stop here
    if len(matches) == 0:
        print("No student found with that name.")
        return None     # None means "nothing found" — the caller checks for this

    # step 4 — show all matched records so the user can see them
    print(f"\n Found {len(matches)} matching record(s):\n")
    for s in matches:
        print(f" ID: {s['id']} | Name: {s['name']} | Age: {s['age']} | Grade: {s['grade']}")

    # step 5 — if only one match, ask to confirm (no need to pick by ID)
    if len(matches) == 1:
        # .strip().lower() makes "Yes", "YES", "yes" all work the same way
        confirm = input(f"\n Only one match found. {action_label.capitalize()} this student? (yes/no): ").strip().lower()
        if confirm == "yes":
            return matches[0]   # return that single student
        else:
            print("Action cancelled.")
            return None

    # step 6 — multiple matches → ask user to pick the exact one by ID
    while True:
        picked_id = input(f"\n Enter the ID of the student you want to {action_label}: ").strip()

        # make sure the input is a number before converting
        if not picked_id.isdigit():
            print("Please enter a valid number ID.")
            continue

        picked_id = int(picked_id)

        # search the matches list for the picked ID
        found = None
        for s in matches:
            if s["id"] == picked_id:
                found = s
                break   # stop looping once we find the match

        if found is None:
            # the ID they typed is not in the list shown above
            print("That ID is not in the list above. Try again.")
            continue

        return found    # user picked a valid student — return it


#  FEATURES

def add_student(students):
    print("\n-- Add Student --\n")

    # PR Review Fix — Critical Bug:
    # The PR version had view logic inside add_student().
    # It was checking "if not students: print no records" and looping through
    # the list — that is view_student()'s job, not add_student()'s.
    # This function must collect input and append a new student. Fixed below.

    name  = get_valid_name("Name  : ")
    age   = get_valid_age("Age   : ")
    grade = get_valid_grade("Grade : ")

    # PR Review Fix #2 — ID duplication bug
    # Old code: id = len(students) + 1
    # Problem scenario:
    #   Add Alice → ID 1, Add Bob → ID 2, Add Carol → ID 3
    #   Delete Bob → list now has 2 students
    #   Add Dave → len is 2, so id = 2+1 = 3 → DUPLICATE with Carol!
    #
    # Fix: find the highest ID currently in the list, then add 1 to it.
    # This way the new ID is always unique, no matter what was deleted.
    if len(students) == 0:
        new_id = 1              # list is empty — start from 1
    else:
        highest_id = 0
        for s in students:
            if s["id"] > highest_id:
                highest_id = s["id"]
        new_id = highest_id + 1     # always one above the current highest

    # Also fixed: "id" was used as a variable name in the PR version.
    # "id" is a built-in Python function — using it as a variable name
    # hides the original. Always use a different name like "new_id".

    students.append({
        "id"    : new_id,
        "name"  : name,
        "age"   : age,      # age is already an int (returned by get_valid_age)
        "grade" : grade
    })

    print(f"\n Student '{name}' added successfully.")


def view_student(students):
    print("\n-- All Students --\n")

    if not students:            # if the list is empty
        print("No records found.")
        return                  # exit the function early — nothing to show

    for i in students:          # loop through every student and print their details
        print(f" ID: {i['id']} | Name: {i['name']} | Age: {i['age']} | Grade: {i['grade']}")


def search_student(students):
    print("\n-- Search Student --\n")

    # block empty search — if name is "", it matches EVERY student
    # because "" (empty string) is always found inside any string
    while True:
        name = input("Enter name to search: ").strip().lower()
        if name == "":
            print("Search name cannot be empty. Please try again.")
        else:
            break

    # find all students whose name contains the search term
    matches = []
    for student in students:
        if name in student["name"].lower():
            matches.append(student)

    if not matches:
        print("No record found.")
        return

    print(f"\n Found {len(matches)} matching record(s):\n")
    for s in matches:
        print(f" ID: {s['id']} | Name: {s['name']} | Age: {s['age']} | Grade: {s['grade']}")


def update_student(students):
    print("\n-- Update Student --\n")

    # find the exact student using the shared helper
    student = find_student_by_name_then_id(students, "update")

    if student is None:
        return      # nothing found or user cancelled — exit early

    # show current details before asking for new values
    print(f"\n Current details:")
    print(f" Name: {student['name']} | Age: {student['age']} | Grade: {student['grade']}")
    print(" (Press Enter to keep the current value)\n")

    # collect new values — empty input means "keep the current value"
    new_name  = input(f" New Name  [{student['name']}]: ").strip()
    new_age   = input(f" New Age   [{student['age']}]: ").strip()
    new_grade = input(f" New Grade [{student['grade']}]: ").strip()

    # PR Review Fix #6 — Note on validation duplication:
    # We cannot directly reuse get_valid_name(), get_valid_age(), get_valid_grade() here
    # because those functions LOOP FOREVER until the user types something valid.
    # But in update, pressing Enter (empty input) means "keep the old value".
    # So we validate manually below — only when the user actually typed something.

    # validate name only if the user typed something
    if new_name != "":
        if not new_name.replace(" ", "").isalpha():
            print("Invalid name. Name was not updated.")
        else:
            student["name"] = new_name

    # validate age only if the user typed something
    if new_age != "":
        # PR Review Fix #4
        # get_valid_age() allows up to 30. Both must use the same range.
        if not new_age.isdigit() or int(new_age) < 1 or int(new_age) > 30:
            print("Invalid age. Age was not updated.")
        else:
            # PR Review Fix #3 — age type inconsistency
            # get_valid_age() returns an int, so add_student stores age as int (e.g. 20)
            # but old update code did: student["age"] = new_age  ← stores "20" (string)
            # This made the JSON inconsistent: some records had age:20, others "20"
            # Fix: always convert to int before storing
            student["age"] = int(new_age)

    # validate grade only if the user typed something
    if new_grade != "":
        new_grade = new_grade.upper()       # make input case-insensitive: "a" → "A"

        # PR Review Fix #5 — now uses global ALLOWED_GRADES constant
        if new_grade not in ALLOWED_GRADES:
            print(f"Invalid grade. Grade was not updated. Allowed: {', '.join(ALLOWED_GRADES)}")
        else:
            student["grade"] = new_grade

    print("\n Student updated successfully.")


def delete_student(students):
    print("\n-- Delete Student --\n")

    # PR Review Fix #1
    # The PR version passed "update" as the action_label:
    #     find_student_by_name_then_id(students, "update")   ← WRONG
    # This caused all delete prompts to say "update" instead of "delete":
    #     "Only one match found. Update this student? (yes/no)"  ← wrong word
    #     "Enter the ID of the student you want to update"       ← wrong word
    # Fix: pass "delete" so the prompts make sense
    student = find_student_by_name_then_id(students, "delete")

    if student is None:
        return      # nothing found or user cancelled — exit early

    # ask for confirmation before permanently removing the record
    # .strip().lower() makes "Yes", "YES", "yes" all work — not just lowercase "yes"
    confirm = input(f"\n Are you sure you want to delete '{student['name']}'? (yes/no): ").strip().lower()

    if confirm == "yes":
        students.remove(student)
        print(f" Student '{student['name']}' deleted successfully.")
    else:
        # PR Review Fix #4 — UX issue: no message shown when user types "no"
        # Without this else, the program silently goes back to the menu.
        # The user needs to know their cancel was received.
        print("Delete cancelled.")


#  MAIN MENU

def main():
    students = load_students()  # load saved data when the program starts

    while True:     # keep showing the menu until the user chooses Exit
        print("\n=== Student Management System ===\n")
        print("1. Add student")
        print("2. View All students")
        print("3. Search student")
        print("4. Update student")
        print("5. Delete student")
        print("6. Save records")
        print("7. Exit\n")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            add_student(students)
        elif choice == "2":
            view_student(students)
        elif choice == "3":
            search_student(students)
        elif choice == "4":
            update_student(students)
        elif choice == "5":
            delete_student(students)
        elif choice == "6":
            save_record(students)
        elif choice == "7":
            save_record(students)       # auto-save before exiting
            print("Exiting the program. Good Bye...!")
            break                       # exits the while loop → program ends
        else:
            print("Invalid option. Try again.")


# this line means: only run main() if this file is run directly
# if another file imports this file, main() will NOT run automatically
if __name__ == "__main__":
    main()