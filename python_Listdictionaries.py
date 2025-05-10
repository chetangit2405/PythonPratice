def salary(employees, typeOperation):
        operType = typeOperation

        for employee in employees:
                if operType == "compare":
                        if int(employee["salary"]) > 50000:
                                print(f"Employee {employee['name']} salary is {employee['salary']}. Salary is morethan 50000.")
                else:
                        print(f"Employee Name {employee['name']} \t| Position {employee['position']}.", end='\n')
                        

employees = [{"name": "Chetan","position":"SE","salary":100000},{"name": "Mamatha","position":"Teacher","salary":150000},{"name": "Sony","position":"staff","salary":10000}]

employees.append({"name": "Chinna","position":"Marketing","salary":90000})

salary(employees, "compare")
print("_______________________________" + '\n')
salary(employees, "listEmployee")

