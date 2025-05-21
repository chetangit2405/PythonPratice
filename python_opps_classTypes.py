"""
1. Abstract Classes
Abstract classes are like blueprints. They can't be instantiated directly and are used to enforce structure for subclasses.

Example:
from abc import ABC, abstractmethod

# Abstract class
class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass

# Subclass must implement abstract method
class Dog(Animal):
    def make_sound(self):
        return "Woof"

class Cat(Animal):
    def make_sound(self):
        return "Meow"

# Test
d = Dog()
c = Cat()
print(d.make_sound())
print(c.make_sound())



2. Class Methods
Class methods work with the class itself, not the instance. They're often used for alternative constructors or class-level operations.

Example:

class Employee:
    company_name = "TechCorp"
    
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    @classmethod
    def from_string(cls, emp_str):
        name, salary = emp_str.split("-")
        return cls(name, int(salary))

    @classmethod
    def get_company_name(cls):
        return cls.company_name

# Usage
emp1 = Employee.from_string("Chetan-50000")
print(emp1.name, emp1.salary)
print(Employee.get_company_name())



3. Static Methods
Static methods don’t use instance or class data. They behave like normal functions but are grouped with the class for relevance.

Example:

class MathUtils:
    @staticmethod
    def add(x, y):
        return x + y

    @staticmethod
    def is_even(n):
        return n % 2 == 0

# Usage
print(MathUtils.add(3, 7))
print(MathUtils.is_even(10))


| Concept        | Keyword                  | Use Case                                 |
| -------------- | ------------------------ | ---------------------------------------- |
| Abstract Class | `ABC`, `@abstractmethod` | Define structure for subclasses          |
| Class Method   | `@classmethod`           | Class-level logic, alternate constructor |
| Static Method  | `@staticmethod`          | Utility/helper methods related to class  |

"""

# Abstract method example
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side * self.side

class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height

# Test
s = Square(4)
t = Triangle(6, 3)
print(f"Square Area: {s.area()}")
print(f"Triangle Area: {t.area()}")


#Class method example.

class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    @classmethod
    def from_string(cls, book_str):
        title, author, year = book_str.split("-")
        return cls(title, author, int(year))

    def display(self):
        print(f"{self.title} by {self.author} ({self.year})")

# Test
b = Book.from_string("Python Basics-John Doe-2020")
b.display()


#static method example
class Validator:
    @staticmethod
    def is_even(n):
        return n % 2 == 0

    @staticmethod
    def is_valid_email(email):
        return "@" in email and "." in email

# Test
print(Validator.is_even(10))           # True
print(Validator.is_valid_email("chetan@example.com"))  # True
print(Validator.is_valid_email("mamatha.com"))         # False