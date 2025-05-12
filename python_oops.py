"""
What Is OOP?
OOP is a programming model where you structure code using classes and objects.

Key Concepts:
| Concept         | Description                                             |
| --------------- | ------------------------------------------------------- |
| **Class**       | A blueprint for creating objects                        |
| **Object**      | An instance of a class                                  |
| **Attributes**  | Variables that belong to an object                      |
| **Methods**     | Functions that belong to an object                      |
| **Constructor** | `__init__()` method that runs when an object is created |
| **Self**        | Refers to the current object                            |

class Student:
    def __init__(self, name, age, marks):
        self.name = name
        self.age = age
        self.marks = marks

    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}, Marks: {self.marks}")

# Create object
s1 = Student("Chetan", 21, 95)

# Call method
s1.display_info()

"""


"""

1. Try modifying this example?

2. Learn how to manage a list of Student objects?

3. Convert your Student Management System functions into a class-based structure?

"""
import csv
import os

students = []

class Student():

    def __init__(self, name, age, marks):
        self.name = name
        self.age = age
        self.marks = marks


    def add_student(name, age, marks):

        students.append({"Name": name, "Age": age, "Marks": marks})
        print(f"Student record added successfully.\n")


    def display_info():
        print("Student records\n")

        if not students:
            print("No students found.\n")
        else:
            for s in students:
                print(f"Name: {s['Name']} | Age: {s['Age']} | Marks: {s['Marks']}")


    def remove_student(name):

        if len(students) == 0:
            print("Student records is empty")

        else:
            found = False
            
            for s in students:
                if s['Name'].lower() == name.lower():
                    students.remove(s)
                    print("Student record removed.\n")

                    found = True
                    break
                
            if not found:
                print("Student not found.\n")


    def search_student(name):
        found = False

        for s in students:
            if s['Name'].lower() == name.lower():
                print(f"Student record found:\n Name: {s['Name']} \t | Age: {s['Age']} \t | Marks: {s['Marks']} \n")
                found = True
                break
            
        if not found:
            print("Student not found.\n")



# Create object
#s1 = Student("Chetan", 21, 95)

# Call method
Student.add_student("Chetan", 21, 95)
Student.add_student("Chinna", 19, 82)
Student.add_student("Mamatha", 20 ,84)
Student.display_info()
Student.remove_student("Chinna")
Student.display_info()
Student.search_student("Mamatha")
Student.search_student("Chinna")


"""

import csv

class Student:
    def __init__(self, name, age, marks):
        self.name = name
        self.age = age
        self.marks = marks

    def display_info(self):
        print(f"Name: {self.name} | Age: {self.age} | Marks: {self.marks}")


class StudentSystem:
    def __init__(self):
        self.students = []

    def add_student(self, name, age, marks):
        student = Student(name, age, marks)
        self.students.append(student)
        print(f"Student {name} added.\n")

    def display_students(self):
        if not self.students:
            print("No students found.\n")
        else:
            print("Student Records:")
            for s in self.students:
                s.display_info()
            print()

    def remove_student(self, name):
        for s in self.students:
            if s.name.lower() == name.lower():
                self.students.remove(s)
                print(f"Student {name} removed.\n")
                return
        print(f"Student {name} not found.\n")

    def search_student(self, name):
        for s in self.students:
            if s.name.lower() == name.lower():
                print("Student found:")
                s.display_info()
                return
        print("Student not found.\n")


# Demo
system = StudentSystem()
system.add_student("Chetan", 21, 95)
system.add_student("Mamatha", 20, 84)
system.add_student("Chinna", 19, 82)

system.display_students()
system.remove_student("Chinna")
system.display_students()
system.search_student("Mamatha")
system.search_student("Chinna")

****** What’s Better Now: ******
Student holds individual data

StudentSystem manages all logic

No global variables

Easier to extend with file I/O, GUI, sorting, etc.

"""