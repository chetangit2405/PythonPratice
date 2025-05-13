"""
Polymorphism Exercise
Task:
Create two classes Circle and Rectangle. Both should have a method area(), but implemented differently:

Circle needs a radius

Rectangle needs width and height

Then, write a function print_area(shape) that takes any shape and prints its area using the area() method.

"""
import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2 # (22/7) *  self.radius * self.radius

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


def print_area(shape):
    print(f"Area: {shape.area()}")

# Example usage
c = Circle(5)
r = Rectangle(4, 6)
print_area(c)
print_area(r)