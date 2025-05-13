"""


"""

class Employee:
    def __init__(self, name, emp_id, base_salary):
        self.name = name
        self.emp_id = emp_id
        self.__salary = base_salary  # Encapsulated attribute

    def get_salary(self):
        return self.__salary

    def set_salary(self, new_salary):
        if new_salary >= 0:
            self.__salary = new_salary
        else:
            print("Invalid salary.")

    def get_bonus(self):
        return 0  # To be overridden

    def display_info(self):
        print(f"Name: {self.name}, ID: {self.emp_id}, Salary: ₹{self.__salary}")


# Inheritance + Polymorphism
class Developer(Employee):
    def __init__(self, name, emp_id, base_salary, tech_stack):
        super().__init__(name, emp_id, base_salary)
        self.tech_stack = tech_stack

    def get_bonus(self):
        return self.get_salary() * 0.10  # 10% bonus

    def display_info(self):
        super().display_info()
        print(f"Role: Developer | Tech Stack: {self.tech_stack} | Bonus: ₹{self.get_bonus()}\n")


class Manager(Employee):
    def __init__(self, name, emp_id, base_salary, team_size):
        super().__init__(name, emp_id, base_salary)
        self.team_size = team_size

    def get_bonus(self):
        return self.get_salary() * 0.15  # 15% bonus

    def display_info(self):
        super().display_info()
        print(f"Role: Manager | Team Size: {self.team_size} | Bonus: ₹{self.get_bonus()}\n")


# Test
dev = Developer("Chetan", 101, 80000, ["Python", "AWS"])
mgr = Manager("Mamatha", 102, 100000, 5)

dev.display_info()
dev.get_bonus()
mgr.display_info()
mgr.get_bonus()