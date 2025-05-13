"""
1. Inheritance
Definition: One class (child) can inherit the properties and methods of another class (parent).

Example:
class Person:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print(f"Hello, I'm {self.name}")

# Student inherits from Person
class Student(Person):
    def __init__(self, name, marks):
        super().__init__(name)  # Call parent constructor
        self.marks = marks

    def show_marks(self):
        print(f"My marks: {self.marks}")

# Usage
s1 = Student("Chetan", 95)
s1.greet()
s1.show_marks()



2. Encapsulation
Definition: Restricting access to internal object details using private variables and methods.

Example:
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance  # Private attribute

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

    def get_balance(self):
        return self.__balance

# Usage
account = BankAccount("Chetan", 1000)
account.deposit(500)
print(account.get_balance())       # Allowed
# print(account.__balance)         # Will raise error


3. Polymorphism
Definition: Methods with the same name behave differently for different classes.

Example 1: Same method name in different classes:

class Dog:
    def speak(self):
        print("Bark!")

class Cat:
    def speak(self):
        print("Meow!")

def make_animal_speak(animal):
    animal.speak()

make_animal_speak(Dog())
make_animal_speak(Cat())


Example 2: Method Overriding:

class Animal:
    def sound(self):
        print("Some generic sound")

class Cow(Animal):
    def sound(self):
        print("Moo")

cow = Cow()
cow.sound()  # Outputs: Moo

"""

"""
Practice:
Create a Vehicle class with attributes brand and year, and a method display_info().

Then, create a Car class that inherits from Vehicle and adds an attribute model. Override display_info() to include the model as well.

"""
# Inheritance
class Vehicle:
    def __init__(self, brand, year):
        self.brand = brand
        self.year = year

    def display_info(self):
        print(f"Brand\t: {self.brand}\nYear\t: {self.year}")

# Car class
class Car(Vehicle):
    def __init__(self, brand, year, model):
        super().__init__(brand, year)
        self.model = model

    def display_info(self):
        super().display_info()
        print(f"Model\t: {self.model}\n")

# Example usage
car = Car("Toyota", 2022, "Corolla")
car.display_info()  # Output: Brand: Toyota, Year: 2022, Model: Corolla
