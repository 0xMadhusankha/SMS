import json
import os

DATA_FILE = "data/students.json"

def load_students():
    return[]

def save_record(students):
    pass

def add_student(students):
    pass

def view_student(students):
    pass

def search_student(students):
    pass

def update_student(students):
    pass

def delete_student(students):
    pass

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
        print("7. Exit")

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