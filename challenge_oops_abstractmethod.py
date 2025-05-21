from abc import ABC, abstractmethod

class Employee(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def calculate_pay(self):
        pass

# ➤ Fill in the classes below
class FullTimeEmployee(Employee):
    def __init__(self, name, monthly_salary):
        super().__init__(name)
        self.monthly_salary = monthly_salary

    def calculate_pay(self):
        return self.monthly_salary

class PartTimeEmployee(Employee):
    def __init__(self, name, hourly_rate, hourly_worked):
        super().__init__(name)
        self.hourly_rate  = hourly_rate
        self.hourly_worked = hourly_worked
    
    def calculate_pay(self):
        return self.hourly_rate * self.hourly_worked

# ➤ Sample test
f = FullTimeEmployee("Chetan", 40000)
p = PartTimeEmployee("Mamatha", 500, 20)

print(f"{f.name} earns: ₹{f.calculate_pay()}")
print(f"{p.name} earns: ₹{p.calculate_pay()}")