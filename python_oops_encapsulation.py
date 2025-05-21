"""
Encapsulation Exercise
Task:
Create a Student class that has a private attribute __grade. Add:

A method to set the grade (only if it's between 0 - 100)

A method to get the grade

"""
class Student:
    def __init__(self, name):
        self.name = name
        self.__grade = None
   
    def set_grade(self, marks):
        if marks >= 0 and marks <= 100 :
            self.__grade = "Pass"
            print("Grade updated.\n")
        else:
            print("Invalid marks. Grade not set.\n")

    def get_grade(self):
        return self.__grade

# Usage
s = Student("Chetan")
s.set_grade(192)
print(f"{s.name} got {s.get_grade()}.\n")