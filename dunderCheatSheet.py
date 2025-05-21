#✅ Python Code to Generate a Dunder Methods Cheat Sheet PDF

from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        self.set_font("Arial", "B", 12)
        self.cell(0, 10, "Python Dunder (Magic) Methods - Cheat Sheet", ln=True, align="C")

    def chapter_title(self, title):
        self.set_font("Arial", "B", 11)
        self.cell(0, 8, title, ln=True, align="L")
        self.ln(2)

    def chapter_body(self, body):
        self.set_font("Arial", "", 10)
        self.multi_cell(0, 6, body)
        self.ln()

content = {
    "Object Lifecycle": """
__init__    - Constructor (called when object is created)
__new__     - Allocates memory, used rarely
__del__     - Destructor (called when object is deleted)
""",
    "String Representation": """
__str__     - Returns readable string (used by print())
__repr__    - Returns unambiguous string (used in shell/debug)
""",
    "Arithmetic Operators": """
__add__     - +
__sub__     - -
__mul__     - *
__truediv__ - /
__floordiv__- //
__mod__     - %
__pow__     - **
__neg__     - Unary -x
""",
    "Comparison Operators": """
__eq__      - ==
__ne__      - !=
__lt__      - <
__le__      - <=
__gt__      - >
__ge__      - >=
""",
    "Type Conversion": """
__int__     - Convert to int
__float__   - Convert to float
__bool__    - Convert to bool
__len__     - Returns length using len(obj)
""",
    "Collection Methods": """
__getitem__ - obj[key]
__setitem__ - obj[key] = value
__delitem__ - del obj[key]
__iter__    - Iteration (for x in obj)
__next__    - Next item in iteration
__contains__- Used with 'in' keyword
""",
    "Attribute Access": """
__getattr__      - Fallback if attribute not found
__setattr__      - Called when attribute is set
__delattr__      - Called when attribute is deleted
__getattribute__ - Intercepts all attribute access
""",
    "Callable & Context Manager": """
__call__    - Makes object callable like a function
__enter__   - Used in with-blocks (entry)
__exit__    - Used in with-blocks (exit)
""",
}

pdf = PDF()
pdf.set_auto_page_break(auto=True, margin=15)
pdf.add_page()

for section, body in content.items():
    pdf.chapter_title(section)
    pdf.chapter_body(body)

pdf.output("python_dunder_methods_cheat_sheet.pdf")