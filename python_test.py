students = []

class Student:
    def __init__(self, name, age, marks):
        self.name = name
        self.age = age
        self.marks = marks

    def display(self):
        print(f"Name: {self.name} | Age: {self.age} | Marks: {self.marks}")

    @classmethod
    def add_student(cls, name, age, marks):
        student = cls(name, age, marks)
        students.append(student)
        print("Student record added successfully.\n")

    @classmethod
    def display_all(cls):
        print("Student Records\n")
        if not students:
            print("No students found.\n")
        else:
            for student in students:
                student.display()

    @classmethod
    def remove_student(cls, name):
        if not students:
            print("Student records are empty.\n")
            return

        for student in students:
            if student.name.lower() == name.lower():
                students.remove(student)
                print("Student record removed.\n")
                return

        print("Student not found.\n")

    @classmethod
    def search_student(cls, name):
        for student in students:
            if student.name.lower() == name.lower():
                print("Student record found:")
                student.display()
                print()
                return

        print("Student not found.\n")

# Example Usage
Student.add_student("Chetan", 21, 95)
Student.add_student("Anita", 22, 88)

Student.display_all()

Student.search_student("Anita")

Student.remove_student("Chetan")

Student.display_all()

s1 = Student("Chinna",16,97)
s1.add_student()
s1.display_all()