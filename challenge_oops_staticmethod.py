"""
[::-1] — What does it do?
This is Python slicing syntax. In general, s[start:stop:step] is the format. When you write s[::-1], you're using:

start: not specified (defaults to the end)

stop: not specified (defaults to the beginning)

step: -1 → this means "step backwards", effectively reversing the sequence.
"""

class Tools:

    @staticmethod
    def is_palindrome(value):
        return str(value) == str(value)[::-1]

    @staticmethod
    def is_positive(num):
        return num > 0
    
"""
@staticmethod
def is_palindrome(value_str): ...
    return value_str == value_str[::-1]

@staticmethod
def is_palindrome(value_num): ...
    return str(value_num) == str(value_num)[::-1]

defining **two static methods with the same name**: is_palindrome`.

This will cause the second one to override the first, so the first one is lost — Python does not support method overloading by argument type.

"""

# ➤ Test
print(Tools.is_palindrome("madam"))   # True
print(Tools.is_palindrome("python"))  # False
print(Tools.is_palindrome(121))         # True
print(Tools.is_palindrome(123))         # False
print(Tools.is_positive(42))          # True
print(Tools.is_positive(-5))          # False