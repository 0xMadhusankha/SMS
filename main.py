import json
import os

DATA_FILE = "data/students.json"

def load_students():
    if os.path.exists(DATA_FILE):               # check if file already exists
        try:                                    # try to open and read the file
            with open(DATA_FILE, "r") as file:
                return json.load(file)          # read and return the data

        except json.JSONDecodeError:
            # this exception is run, when the file exists but content is corrupted
            print("Warning: student.json is corrupted and could not be read.")
            print("Statring with an empty student list.")
            return []                           # then create empty student list

    return[]                                    # if the file dosent exist yet, fresh start                                    
            
def save_record(students):
    os.makedirs("data", exist_ok=True)          # create data folder if its missing
    with open(DATA_FILE, "w") as file:
        json.dump(students, file, indent=4)     # write data to file

    print("Records saved successfully.")



# ==========    INPUT validation    ==========
def get_valid_name(prompt):
    while True:
        name = input(prompt).strip()

        if name == "":                                                  # check if the name field is empty
            print("Name cannot be empty. Please try again")
            continue

        if not name.replace(" ", "").isalpha():                         # check if user enter name field contain numbers - replace(" ", "") this line removes the spaces on name field.
            print("Name should only contain letters. Please try again")
            continue

        return name                                                     # return valid name

def get_valid_age(prompt):
    while True:
        age = input(prompt).strip()

        if age == "":                       # check if the age field is empty
            print("Age cannot be empty. Please try again")
            continue

        if not age.isdigit():               # check if user enter age field contain letters
            print("Age must be a number (e.g. 20). Please try again")
            continue

        age_number = int(age)

        if age_number < 1 or age_number > 30:
            print("Please enter valid age (1 - 29)")
            continue

        return age_number                   # return the age as int


def get_valid_grade(prompt):
    allowed_grade = ["A+", "A", "A-", "B+", "B", "B-", "C+", "C", "C-", "D+", "D", "D-", "F"]

    while True:
        grade = input(prompt).strip().upper()                                           # .upper() - "a" becomes "A", "b+" becomes "B+"                                  

        if grade == "":
            print("Grade cannot be empty. Please try again.")
            continue

        if grade not in allowed_grade:
            print(f"Invalid grade. Allowed grades: {','.join(allowed_grade)}")          # {','.join(allowed_grade)} - if entered grade is invalid show the valid grade list
            continue

        return grade

# helper finction for find students by name, then let the user pock one by ID
# if we search by name, it can be duplicate. so this function helps to get actual data

def find_student_by_name_then_id(students, action_label):       # the action_label is search, update or delete function 
    # step 1 - ask for a name and show all matches.
    while True:
        name = input("Enter name to search: ").strip().lower()
        if name == "":     # check if user input is blank
            print("search name cannot be empty. Please try again")
            continue
        else:
            break           # valid input, exit the wihle loop

    # step 2 - find the all students whoes name contains user input

    matches = []                                # create a empty list for store filtred data
    for student in students:
        if name in student["name"].lower():     # get the student names with lowercase
            matches.append(student)             # put all matched records to empty list
    
    if len(matches) == 0:                       # if nothing found stop 
        print("No student found with that name")
        return None

    # step 3 - show all match records
    print(f"\n Found {len(matches)} matching records:\n")
    for s in matches:
        print(f"ID: {s['id']} | Name: {s['name']} | Age: {s['age']} | Grade: {s['grade']}")

    # step 4 - if only one match, ask to confirm instead of picking
    if len(matches) == 1:
        confirm = input(f"Only one match found. {action_label.capitalize()} this student? (yes/no)").strip().lower()
        if confirm == "yes":
            return matches[0]
        else:
            print("Action cancelled.")
            return None

    # Step 5 -if multiple matches, ask user to pick by ID
    while True:
        picked_id = input(f"\n Enter the ID of the student you want to {action_label}: ").strip()

        if not picked_id.isdigit():
            print("Please enter a valid number ID")
            continue

        picked_id = int(picked_id)

        found = None
        for s in matches:
            if s["id"] == picked_id:
                found = s
                break

        if found is None:
            print("That ID is not in the list above. Try again.")
            continue

        return found        # return valid ID

# ========== Features =========

def add_student(students):
    print("\n-- Add Student --\n")

    name = get_valid_name("Name : ")
    age = get_valid_age("Age : ")
    grade = get_valid_grade("Grade : ")
    id = len(students) + 1              # auto generate the student ID

    students.append({
        "id" : id,
        "name" : name,
        "age" : age,
        "grade" : grade
    })

    print(f"Student '{name}' added successfully.")

def view_student(students):
    print("\n-- All students --\n")

    if not students:                # if list is empty show no record found
        print("No records found.")
        return                      # safely exit the function

    for i in students:              # loop every student and print it
        print(f"ID: {i['id']} | Name: {i['name']} | Age: {i['age']} | Grade: {i['grade']}")

def search_student(students):
    print("\n--- Search Student --\n")

    while True:
        name = input("Enter name to search: ").strip().lower()
        if name == "":
            print("Search name cannot be empty. Please try again")
        else:
            break

    matches = []
    for student in students:
        if name in student["name"].lower():
            matches.append(student)

    if not matches:
        print(" No record found.")
        return

    print(f"\n Found {len(matches)} matching records:\n")
    for s in matches:
        print(f" ID: {s['id']} | Name: {s['name']} | Age: {s['age']} | Grade: {s['grade']}")


def update_student(students):
    print("\n-- Update student --")

    student = find_student_by_name_then_id(students, "update")

    if student is None:
        return

    print(f"\nCurrent details:")
    print(f" Name: {student['name']} | Age: {student['age']} | Grade: {student['grade']}")
    print(" (Press Enter to keep the current value)\n")

    # ask new values - empty field mean keep the old value
    new_name  = input(f"  New Name  [{student['name']}]: ").strip()
    new_age   = input(f"  New Age   [{student['age']}]: ").strip()
    new_grade = input(f"  New Grade [{student['grade']}]: ").strip()

    # validate new name
    if new_name != "":
        if not new_name.replace(" ", "").isalpha():
            print("Invalid name. Name was not updated")
        else:
            student["name"] = new_name
    
    # validate new age
    if new_age != "":
        if not new_age.isdigit() or int(new_age) < 1 or int(new_age) > 30:
            print("Invalid age. Age was not updated")
        else:
            student["age"] = new_age
    
    # validate new grade
    if new_grade != "":
        allowed_grades = ["A+", "A", "A-", "B+", "B", "B-", "C+", "C", "C-", "D+", "D", "D-", "F"]
        new_grade = new_grade.upper()       # make the grade uppercase

        if new_grade not in allowed_grades:
            print(f"  ⚠  Invalid grade. Grade was not updated. Allowed: {', '.join(allowed_grades)}")
        else:
            student["grade"] = new_grade
            
    print("\nStudent updated successfully.")

def delete_student(students):
    print("\n-- Delete student --")
    
    student = find_student_by_name_then_id(students,"update")

    if student is None:
        return              # nothing found or user cancelled

    # confirm before delete
    confirm =  input(f"\n  Are you sure you want to delete '{student['name']}'? (yes/no): ").strip().lower()

    if confirm == "yes":
        students.remove(student)
        print(f" Student '{student['name']}' deleted successfully.")

def main():

    students = load_students()

    while True:
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
            save_record(students)
            print("Exiting the program. Good Bye...!")
            break
        else:
            print("Invalid option. Try again.")

if __name__ == "__main__":
    main()