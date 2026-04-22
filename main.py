import json
import os

DATA_FILE = "data/students.json"

def load_students():
    if os.path.exists(DATA_FILE):           # check if file already exists
        with open(DATA_FILE, "r") as file:
            return json.load(file)          # read and return the data
    return []                               # if no file yet, return empty list

def save_record(students):
    os.makedirs("data", exist_ok=True)      # create data folder if its missing
    with open(DATA_FILE, "w") as file:
        json.dump(students, file, indent=4) # write data to file

    print("Records saved successfully.")

def add_student(students):
    print("\n-- Add Student --\n")
    name = input("Name: ").strip()      # .strip remove extra spaces
    age = input("Age: ").strip()
    grade = input("Grade: ").strip()
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