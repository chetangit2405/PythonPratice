"""
"with" handles closing the file automatically.

"w" means write mode — it creates the file or overwrites if it exists.
"r" is read mode.
"a" means append mode — it adds content to the end.

Syntax:
with open("demo.txt", "w") as file:
with open("demo.txt", "r") as file:
with open("demo.txt", "a") as file:


Examples:

1. Writing to a File

with open("demo.txt", "w") as file:
    file.write("Hello, this is the first line.\n")
    file.write("And this is the second line.")


2. Reading from a File

with open("demo.txt", "r") as file:
    content = file.read()
    print(content)


3. Appending to a File

with open("demo.txt", "a") as file:
    file.write("\nThis is an appended line.")


4. Reading Line by Line

with open("demo.txt", "r") as file:
    for line in file:
        print(line.strip())  # .strip() removes newline characters


5. Checking if File Exists (Optional)

import os

if os.path.exists("demo.txt"):
    print("File exists.")
else:
    print("File not found.")


"""



"""
Exercise:

Write the following lines to a file called students.txt:

"Chetan - 92"

"Mamatha - 88"

"Ravi - 79"

Read the file and print each line with:
"Student Info: <line content>"

"""


import os

def fileOperation(filepath, filework):
    if os.path.exists("student.txt"):
        #print("File exists.")

        if filework == "write":
            with open(filepath, "w") as file:
                #file.clear()
                file.write("Chetan - 92\nMamatha - 88\nRavi - 79")
                print("File write completed.")
                
        elif filework == "read":
            with open(filepath, "r") as file:
                doc = file.read()
                print(f"Student Info:\n{doc}")
                print("File read completed.\n")
                
        elif filework == "append":
            with open(filepath, "a") as file:
                file.write("\nRama - 100")
                print("File appended.\n")

    else:
        print("File not found.\n")



filepath = "student.txt"

fileOperation(filepath, "write")
fileOperation(filepath, "append")
fileOperation(filepath, "read")
