"""
1. @property — Accessing methods like variables

Normally, if you want to get a computed value, you call a method:

class Square:
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2

s = Square(4)
print(s.area())  # Outputs: 16


With @property, you can access the result like an attribute, not like a method:

class Square:
    def __init__(self, side):
        self._side = side  # leading underscore = "internal use"

    @property
    def area(self):
        return self._side ** 2

s = Square(4)
print(s.area)  # ✅ No parentheses, still gives 16


✔ Why is this useful?
You get the simplicity of attributes (no need to remember ())

You can hide internal logic behind an easy-to-use interface



**Add a setter using @property_name.setter

class Square:
    def __init__(self, side):
        self._side = side

    @property
    def area(self):
        return self._side ** 2

    @area.setter
    def area(self, new_area):
        # if you set area, calculate the new side
        self._side = (new_area) ** 0.5

s = Square(4)
print(s.area)      # 16
s.area = 25        # sets side to √25 = 5
print(s.area)      # 25



2. Operator Overloading — Custom behavior for operators
Python allows you to define how built-in operators (+, -, ==, etc.) behave for your custom objects using special methods (also called dunder methods, like __add__ and __str__).

__add__ — customize + between two objects

class Money:
    def __init__(self, amount):
        self.amount = amount

    def __add__(self, other):
        return Money(self.amount + other.amount)

    def __str__(self):
        return f"₹{self.amount}"

wallet1 = Money(100)
wallet2 = Money(150)

wallet3 = wallet1 + wallet2  # Calls __add__
print(wallet3)               # Calls __str__ → ₹250


🎨 __str__ — customize how print() shows your object

Without __str__, printing your object shows an ugly memory address:

m = Money(200)
print(m)  # <__main__.Money object at 0x...>


With __str__, you control how it displays:

def __str__(self):
    return f"₹{self.amount}"

Using __str__ directly we can use method (Money()) to display result.
print(Money(200))  # ₹200



| Feature     | What it does                              | Syntax Example                         |
| ----------- | ----------------------------------------- | -------------------------------------- |
| `@property` | Treat a method as an attribute            | `@property` and `@attr.setter`         |
| `__str__`   | Customize how your object is printed      | `def __str__(self): return ...`        |
| `__add__`   | Customize behavior of `+` between objects | `def __add__(self, other): return ...` |


"""

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    @property
    def area(self):
        return self.length * self.width
    
    def __str__(self):
        return f"Rectangle: {self.length} * {self.width}"
    
    def __add__(self, other):
        return Rectangle((self.length + other.length) , max(self.width, other.width))
    

# ✅ Test
r1 = Rectangle(10, 5)
r2 = Rectangle(6, 7)
r3 = r1 + r2

print(r1)              # Calls __str__ o/p: Rectangle: 10 x 5
print(r2)              # Calls __str__ o/p: Rectangle: 6 x 7
print(r3)              # Calls __str__ o/p: Rectangle: 16 x 7
print(r3.area)         # Calls __add__ o/p: 112


"""_________another example: Temperature__________"""

class Temperature:
    def __init__(self, celsius):
        self._celsius = celsius

    @property
    def celsius(self):
        return self._celsius

    @celsius.setter
    def celsius(self, value):
        if value < -273.15:
            raise ValueError("Temperature can't go below absolute zero!")
        self._celsius = value

    @property
    def fahrenheit(self):
        return (self._celsius * 9/5) + 32

    def __str__(self):
        return f"Temperature: {self._celsius}°C / {self.fahrenheit}°F"

    def __add__(self, other):
        if isinstance(other, Temperature):
            return Temperature(self.celsius + other.celsius)
        return NotImplemented

t1 = Temperature(25)
t2 = Temperature(10)
t3 = t1 + t2

print(t1)  # Temperature: 25°C / 77.0°F
print(t2)  # Temperature: 10°C / 50.0°F
print(t3)  # Temperature: 35°C / 95.0°F

t3.celsius = 100  # Should raise ValueError


"""___________Another example: Money_____________"""

class Money:
    def __init__(self, amount, currency):
        self._amount = amount
        self.currency = currency.upper()

    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, value):
        if value < 0:
            raise ValueError("Amount cannot be negative.")
        self._amount = value

    def __str__(self):
        symbol = {
            "USD": "$",
            "INR": "₹",
            "EUR": "€"
        }.get(self.currency, "")
        return f"{symbol}{self.amount:.2f}"

    def __add__(self, other):
        if isinstance(other, Money):
            if self.currency == other.currency:
                return Money(self.amount + other.amount, self.currency)
            raise ValueError("Cannot add amounts with different currencies.")
        return NotImplemented

    def __eq__(self, other):
        if isinstance(other, Money):
            return self.amount == other.amount and self.currency == other.currency
        return NotImplemented


# ✅ Test
m1 = Money(500, "INR")
m2 = Money(200, "INR")
m3 = m1 + m2

print(m1)           # ₹500.00
print(m2)           # ₹200.00
print(m3)           # ₹700.00
print(m1 == m2)     # False

m4 = Money(500, "INR")
print(m1 == m4)     # True

# Uncomment below to test error
m5 = Money(300, "USD")
m6 = m1 + m5  # ❌ Raises ValueError: Cannot add amounts with different currencies.