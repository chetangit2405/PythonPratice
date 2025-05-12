"""

Mini Project: Student Management System (Console-Based)

Use:
Functions

Lists of dictionaries

File handling (CSV)

Conditional logic

Loops

Input/output


Project Description:
Build a simple system where you can:

Add a student with name, age, and marks

Display all students

Search student by name

Save data to a CSV file

Load data from CSV file


Exercise:
Deleting a student

Updating a student’s marks

Sorting students by marks

"""

import csv

students = []

def add_student():
    name = input("Enter name: ")
    age = input("Enter age: ")
    marks = input("Enter marks: ")

    students.append({"Name" : name, "Age": age, "Marks": marks})
    print("Student record added.\n")


def display_students():
    if not students:
        print("No students found.\n")
    else:
        for s in students:
            print(f"Name: {s['Name']} | Age: {s['Age']} | Marks: {s['Marks']}")

        
def search_student():
    searchName = input("Enter student name to search: ")
    found = False

    for s in students:
        if s['Name'].lower() == searchName.lower():
            print(f"Student record found:\n Name: {s['Name']} \t | Age: {s['Age']} \t | Marks: {s['Marks']} \n")
            found = True
            break
        
    if not found:
        print("Student not found.\n")


def save_to_file():
    with open("students_data.csv", "w", newline="") as file:

        writer = csv.DictWriter(file, fieldnames=["Name", "Age", "Marks"])
        writer.writeheader()
        writer.writerows(students)
    print("Data saved to students_data.csv\n")


def load_from_file():
    global students
    try:
        with open("students_data.csv", "r") as file:
            reader = csv.DictReader(file)
            students = list(reader)
        print("Data loaded from file.\n")
    except FileNotFoundError:
        print("No file found. Starting with empty data.\n")

def update_student():

    if len(students) == 0:
        print("Student records is empty")

    else:
        studentName = input("Enter student name to update marks: ")
        found = False
        
        for s in students:
            if s['Name'].lower() == studentName.lower():
                updateMarks = input(f"Enter new marks to {s['Name']}:")

                s['Marks'] = updateMarks

                print("Marks updated\n")
                found = True
                break

        if not found:
            print("Student not found.\n")


def remove_student():

    if len(students) == 0:
        print("Student records is empty")

    else:
        studentName  = input("Enter student name to update marks: ")
        found = False
        
        for s in students:
            if s['Name'].lower() == studentName.lower():
                students.remove(s)
                print("Student record removed.\n")

                found = True
                break
            
        if not found:
            print("Student not found.\n")


def sort_student(sortType, orderType):

    if len(students) == 0:
        print("Student records is empty")

    else:       
        if sortType == "name" and orderType == "asc":
            students.sort(key=lambda student: student['Name'])
            print(f"Sorted records on Name in asc order: \n {students}")
            
        elif sortType == "name" and orderType == "desc":
            students.sort(key=lambda student: student['Name'], reverse=True)
            print(f"Sorted records on Name in dec order: \n {students}")
            
        elif sortType == "age" and orderType == "asc":
            students.sort(key=lambda student: student['Age'])
            print(f"Sorted records on Age in asc order: \n {students}")
            
        elif sortType == "age" and orderType == "desc":
            students.sort(key=lambda student: student['Age'], reverse=True)
            print(f"Sorted records on Age in desc order: \n {students}")
            
        elif sortType == "marks" and orderType == "asc":
            students.sort(key=lambda student: student['Marks'])
            print(f"Sorted records on Marks in asc order: \n {students}")
            
        elif sortType == "marks" and orderType == "desc":
            students.sort(key=lambda student: student['Marks'], reverse=True)
            print(f"Sorted records on Marks in desc order: \n {students}")
            
        else:
            print("Invalid sort option selected.\n")


"""

students = [
    {"name": "Chetan", "age": 16, "marks": 77},
    {"name": "Mamatha", "age": 17, "marks": 87},
    {"name": "Chinna", "age": 18, "marks": 97}
]

def sort_student(sortType, orderType):
    if not students:
        print("Student records are empty")
        return

    valid_keys = {"name", "age", "marks"}
    valid_orders = {"asc", "desc"}

    if sortType not in valid_keys or orderType not in valid_orders:
        print("Invalid sort option selected.\n")
        return

    reverse = (orderType == "desc")
    students.sort(key=lambda student: student[sortType], reverse=reverse)
    
    print(f"Sorted records by '{sortType}' in {orderType.upper()} order:\n")
    for student in students:
        print(student)

# Example usage
sort_student("marks", "desc")


"""

def menu():
    load_from_file()
    while True:
        print("1. Add Student")
        print("2. Display All Students")
        print("3. Search Student by Name")
        print("4. Save to File")
        print("5. Update student Marks")
        print("6. Remove student")
        print("7. Sort students")
        print("8. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            add_student()
        elif choice == "2":
            display_students()
        elif choice == "3":
            search_student()
        elif choice == "4":
            save_to_file()
        elif choice == "5":
            update_student()
        elif choice == "6":
            remove_student()
        elif choice == "7":
            sortType = input("On what criteria you want to sort (name / age / marks):")
            orderType = input("Enter sorting order (asc / desc):")
            sort_student(sortType, orderType)
        elif choice == "8":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Try again.\n")

menu()
