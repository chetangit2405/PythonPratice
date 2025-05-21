"""
comparison operator overloading in Python using special methods like:

__eq__: Equal to ==

__lt__: Less than <

__le__: Less than or equal to <=

__gt__: Greater than >

__ge__: Greater than or equal to >=

__ne__: Not equal to !=



All Python Dunder methods:

Dunder methods (short for Double UNDERSCORE) in Python are special methods with names like __init__, __str__, __add__, etc. They're also called magic methods and are used to define how objects behave with built-in operations (like printing, arithmetic, iteration, comparison, etc.).

🛠 Object Lifecycle

| Method     | Purpose                                     |
| ---------- | ------------------------------------------- |
| `__init__` | Constructor – called when object is created |
| `__new__`  | Creates a new instance (rarely overridden)  |
| `__del__`  | Destructor – called when object is deleted  |



📦 String Representation

| Method     | Purpose                                 |
| ---------- | --------------------------------------- |
| `__str__`  | User-friendly string (`print(obj)`)     |
| `__repr__` | Unambiguous string (`repr(obj)`, shell) |

Sample:
def __str__(self):
    return f"Name: {self.name}"

def __repr__(self):
    return f"Person('{self.name}')"


    
➕ Arithmetic Operations

| Method         | Operator   |
| -------------- | ---------- |
| `__add__`      | `+`        |
| `__sub__`      | `-`        |
| `__mul__`      | `*`        |
| `__truediv__`  | `/`        |
| `__floordiv__` | `//`       |
| `__mod__`      | `%`        |
| `__pow__`      | `**`       |
| `__neg__`      | Unary `-x` |

Example:
def __add__(self, other):
    return Rectangle(self.length + other.length, self.width + other.width)

    

🔁 Comparison Operators

| Method   | Operator |
| -------- | -------- |
| `__eq__` | `==`     |
| `__ne__` | `!=`     |
| `__lt__` | `<`      |
| `__le__` | `<=`     |
| `__gt__` | `>`      |
| `__ge__` | `>=`     |

Example:
def __eq__(self, other):
    return self.name == other.name

    

📚 Type Conversion & Representation

| Method      | Purpose             |
| ----------- | ------------------- |
| `__int__`   | Convert to `int`    |
| `__float__` | Convert to `float`  |
| `__bool__`  | Convert to `bool`   |
| `__len__`   | Length (`len(obj)`) |



📦 Collection & Indexing

| Method         | Purpose                     |
| -------------- | --------------------------- |
| `__getitem__`  | Access item `obj[key]`      |
| `__setitem__`  | Set item `obj[key] = value` |
| `__delitem__`  | Delete item `del obj[key]`  |
| `__iter__`     | Iterator (`for x in obj`)   |
| `__next__`     | Next item (`next(obj)`)     |
| `__contains__` | Membership (`in` operator)  |

Example:
def __getitem__(self, index):
    return self.data[index]


📛 Attribute Access

| Method             | Purpose                         |
| ------------------ | ------------------------------- |
| `__getattr__`      | Called if attribute not found   |
| `__setattr__`      | Called on attribute assignment  |
| `__delattr__`      | Called on attribute deletion    |
| `__getattribute__` | Intercepts all attribute access |



📞 Callable & Context Manager

| Method      | Purpose                           |
| ----------- | --------------------------------- |
| `__call__`  | Makes object callable like a func |
| `__enter__` | With-statement entry              |
| `__exit__`  | With-statement exit               |

Example:
def __call__(self, x):
    return x * 2


📚 Class-Related

| Method      | Purpose                 |
| ----------- | ----------------------- |
| `__class__` | Get class of object     |
| `__mro__`   | Method Resolution Order |
| `__bases__` | Base classes of a class |


Example: Custom Class with Dunder Methods

class Book:
    def __init__(self, title, pages):
        self.title = title
        self.pages = pages

    def __str__(self):
        return f"📘 {self.title}"

    def __len__(self):
        return self.pages

    def __add__(self, other):
        return Book(f"{self.title} & {other.title}", self.pages + other.pages)

b1 = Book("Python Basics", 300)
b2 = Book("OOP in Depth", 250)
print(b1)               # 📘 Python Basics
print(len(b1))          # 300
print((b1 + b2).title)  # Python Basics & OOP in Depth



✅ Summary of Common Dunder Methods
| Category           | Examples                            |
| ------------------ | ----------------------------------- |
| Constructor        | `__init__`, `__del__`               |
| String             | `__str__`, `__repr__`               |
| Arithmetic         | `__add__`, `__sub__`, etc.          |
| Comparison         | `__eq__`, `__lt__`, etc.            |
| Conversion         | `__int__`, `__bool__`               |
| Collection         | `__getitem__`, `__iter__`, etc.     |
| Attribute Access   | `__getattr__`, `__setattr__`        |
| Callable / Context | `__call__`, `__enter__`, `__exit__` |



"""


class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f"{self.name} - ₹{self.price}"

    def __eq__(self, other):
        return self.price == other.price

    def __lt__(self, other):
        return self.price < other.price

    def __le__(self, other):
        return self.price <= other.price

    def __gt__(self, other):
        return self.price > other.price

    def __ge__(self, other):
        return self.price >= other.price

    def __ne__(self, other):
        return self.price != other.price


p1 = Product("Phone", 25000)
p2 = Product("Tablet", 30000)
p3 = Product("Phone", 25000)

print(p1)               # Phone - ₹25000
print(p2)               # Tablet - ₹30000

print(p1 == p3)         # True
print(p1 != p2)         # True
print(p1 < p2)          # True
print(p2 > p1)          # True
print(p1 >= p3)         # True
print(p1 <= p2)         # True


"""__________________Another example: Books___________________"""

class Book:
    def __init__(self, bookname, author, pages):
        self.bookname = bookname
        self.author = author
        self.pages = int(pages)

    def __str__(self):
        return f"Book: {self.bookname} by {self.author} [{self.pages} pages].\n"
    
    def __eq__(self, other):
        #return self.bookname == other.bookname and self.author == other.author and self.pages == other.pages
        return self.pages == other.pages
    
    def __lt__(self, other):
        return self.pages < other.pages

    def __gt__(self, other):
        return self.pages > other.pages    

b1 = Book("The Alchemist", "Paulo Coelho", 197)
b2 = Book("Harry Potter", "J.K. Rowling", 500)
b3 = Book("The Alchemist", "Paulo Coelho", 197)

print(b1)              # Book: The Alchemist by Paulo Coelho [197 pages]
print(b1 == b3)        # True
print(b1 < b2)         # True
print(b2 > b1)         # True
print(b1 == b2)        # False