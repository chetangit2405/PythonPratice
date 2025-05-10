numbers = [10, 2, 33, 24, 30]

print(numbers[1:4]) #Print values 2,33,24 here index values will be taken

print("Without sorted: ", numbers)

numbers.sort()

print("Numbers sorted: ", numbers)

numbers.sort(reverse=True)
print("Numbers in decending order: ", numbers)

"""
number_sort = number.sort()
print("Numbers sorted: ", numbers_sort)

number_sort = number.sort(reverse=True)
print("Numbers sorted: ", numbers_desc)

This will give output as NONE. Because

Sorting with sort(): The sort() method sorts the list in place, which means it modifies the original list and does not return a new sorted list. So, instead of assigning it to a new variable (like numbers_sort), you directly use numbers.sort() and print numbers after sorting.

Sorting in descending order: You correctly used the reverse=True argument, but instead of saving it into a new variable (numbers_dec), you can directly print numbers after sorting in reverse.


To assign sorted values to variables. Follow below approach.
"""


groceries_list = ["Apples", "Pens", "Chocolates", "Biscuts", "Eclairs", "Chicken", "Drinks"]

print("Groceries list: ", groceries_list)

groceries_sort = sorted(groceries_list)
print("Groceries list sorted: ", groceries_sort)

groceries_dec = sorted(groceries_list, reverse=True)
print("Groceries list sorted desc: ", groceries_dec)
