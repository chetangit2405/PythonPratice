"""
Python has a built-in module called csv that makes working with .csv files simple.


1. Writing to a CSV File

import csv

with open("students.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Name", "Marks"])  # Header row
    writer.writerow(["Chetan", 92])
    writer.writerow(["Mamatha", 88])
    writer.writerow(["Ravi", 79])


#Note: newline="" avoids extra blank lines on Windows.


2. Reading from a CSV File

import csv

with open("students.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(" | ".join(row))


3. Writing a CSV Using Dictionaries

with open("students_dict.csv", "w", newline="") as file:
    fieldnames = ["Name", "Marks"]
    writer = csv.DictWriter(file, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerow({"Name": "Chetan", "Marks": 92})
    writer.writerow({"Name": "Mamatha", "Marks": 88})


4. Reading CSV as Dictionaries

with open("students_dict.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(f"{row['Name']} scored {row['Marks']}")


"""

"""

Practice Task:
Create a CSV file employees.csv with headers: "Name", "Position", "Salary".

Add 3 rows of data using csv.DictWriter.

Read and print each row using csv.DictReader in the format:
"Name is a Position earning Salary."

"""



import csv

with open("employees.csv", "w", newline ="") as file:
    fieldNames = ["Name", "Position", "Salary"]

    writer = csv.DictWriter(file, fieldnames=fieldNames)
    writer.writeheader()
    writer.writerow({"Name": "Chetan", "Position": "SE", "Salary": 100000})
    writer.writerow({"Name": "Mamatha", "Position": "Teacher", "Salary": 110000})
    writer.writerow({"Name": "Chinna", "Position": "Marketing", "Salary": 90000})

with open("employees.csv", "r", newline ="") as file:
    reader = csv.DictReader(file)

    for row in reader:
        print(f"{row['Name']} is {row['Position']} Position earning salary {row['Salary']}/-.")
