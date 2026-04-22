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
    name = input("Enter name to search: ").strip().lower()
    result = []

    for student in students:                        # looping the student list
        student_name = student["name"].lower()

        if name in student_name:                    # check if user input is match
            result.append(student)                  # add matched student details to list
    
    if result:
        for s in result:
            print(f"\nID: {s['id']} | Name: {s['name']} | Age: {s['age']} | Grade: {s['grade']}")   # print the results
    else:
        print("No record found.")

def update_student(students):
    print("\n-- Update student --")
    name = input("Enter name of student to update: ").strip().lower()
    for student in students:
        if student["name"].lower() == name:     # check if user entered student exit
            print(f"Current: Name: {student['name']} | Age: {student['age']} | Grade: {student['grade']}")  # if the student exit print current details
            new_age = input("Enter New Age (press enter to keep current): ").strip()
            new_grade = input("Enter New Grade (press enter to keep current): ").strip()

            if new_age:                         # check if user enter the new data
                student['age'] = new_age        # if new data found update it
            if new_grade:
                student['grade'] = new_grade
            print("Student Update successfully.")
            return
    print("Student not found")

def delete_student(students):
    print("\n-- Delete student --")
    name = input("Enter name of student to delete: ").strip().lower()

    for student in students:
        if student["name"].lower() == name:
            students.remove(student)
            print(f"Student '{student['name']}' deleted.")
            return
    print("Student not found.")


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