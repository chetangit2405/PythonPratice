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

    def update_marks(self, name, updatemarks):
        for s in self.students:
            if s.name.lower() == name.lower():
                s.marks = updatemarks
                print("Student marks updated.\n")
                s.display_info()
                return
        print("Student not found.\n")


    def download_report(self, reportType):
        
        if len(self.students) == 0:
            print("No student records found.\n")
            return

        if reportType.lower() == "csv":
            filename="student_report.csv"
            
            try:
                with open(filename, mode="w", newline="") as file:
                    writer = csv.writer(file)
                    writer.writerow(["Name", "Age", "Marks"])  # Header
                    for student in self.students:
                        writer.writerow([student.name, student.age, student.marks])
                print(f"CSV report saved to {filename}\n")
            
            except Exception as e:
            
                print(f"Failed to write CSV report: {e}")

        elif reportType.lower() == "txt":
            filename="student_report.txt"

            try:
                with open(filename, mode="w") as file:
                    file.write("Student Report:\n__________________\n\n")
                    file.write(f"Name\t|Age\t|Marks\n")

                    for student in self.students:
                        file.write(f"{student.name}\t|{student.age}\t|{student.marks}\n")
                        print(f"Report saved to {filename}\n")

            except Exception as e:
                print(f"Failed to write report: {e}")


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
system.update_marks("Mamatha",85)
system.download_report("txt")
system.download_report("csv")