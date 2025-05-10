"""
What Is a Lambda Function?
A lambda function is a small, anonymous function that’s defined without a name using the lambda keyword. It's usually used for short, simple operations — especially when passing functions as arguments.

Syntax:
lambda arguments: expression


add = lambda a, b: a + b
print(add(3, 5))  # Output: 8


def add(a, b):
    return a + b

add(3,5) #Above and this function both are same.

"""


mul = lambda a,b: a*b
add = lambda a,b: a+b
sub = lambda a,b: a-b
mod = lambda a,b: a%b

print(mul(5,8))
print(add(5,16))
print(sub(5,24))
print(mod(25,5))

#___________________

students = [
    {"name": "Chetan", "marks": 92},
    {"name": "Mamatha", "marks": 85},
    {"name": "Ravi", "marks": 78}
]

# Sort by marks
sorted_students = sorted(students, key=lambda student: student["marks"], reverse=True)
print(sorted_students)


#___________________

#Lambda with filter()
numbers = [1, 2, 3, 4, 5, 6]
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(evens)  # Output: [2, 4, 6]


#Lambda with map()
numbers = [1, 2, 3, 4, 5]
squares = list(map(lambda x: x * x, numbers))
print(squares)  # Output: [1, 4, 9, 16, 25]


"""
Exercise:
Use a lambda function to multiply two numbers.

Use map() and a lambda to double all numbers in a list.

Use filter() and a lambda to get all numbers divisible by 3 from a list.

"""

mul = lambda a,b: a*b
print(mul(5,8))


numbers = [1, 2, 3, 4, 5, 6]
doubleNum = list(map(lambda x: 2*x, numbers))
print("Number double :", doubleNum)

divBy3 = list(filter(lambda x: x%3 == 0, numbers))
print("Number divisible by 3 :", divBy3)
