'''
Dictionaries store data in key-value pairs.
'''

profile = {"Name":"Chetan","Age":37,"Location":"India"}

print(profile["Name"])

profile["Name"] = "Chetan Kumar" #modify value

print(profile["Name"])


#Adding and removing key-value
profile["Profession"] = "SE"
del profile["Location"]


#Loop dictionary values
for key,value in profile.items():
    print(f"key: {key} | value: {value}")



#check key present

if "Name" in profile:
    print("Name key present")


"""
Student record.
"""

student ={"name":"Mamatha","grade":"A","marks":96}
print(student["marks"])

student["passed"]= True

for key,value in student.items():
    print(f"key: {key} | value: {value}")


"""
Dictionaries inside list
"""

