"""
Tuples are used for grouping data in Python. They are ordered, immutable, and written with round brackets. Once a tuple is created, its elements cannot be changed, added, or removed. Tuples are similar to lists, but their immutability conveys that the data within should not be modified. This characteristic allows for potential optimizations in code execution, making tuples slightly faster than lists.
"""

my_tuple = ("a", "b", "c")
print(my_tuple[1])


#Concatenate and repeat tuples

tuple1 = (1,2)
tuple2 = (3,4)

print(tuple1 + tuple2) #Concatenate
print(tuple1 * 2) #Repeat


#Tuple unpacking
cordinates = (13.4, 21.7)
x, y = cordinates
print(x)
print(y)
