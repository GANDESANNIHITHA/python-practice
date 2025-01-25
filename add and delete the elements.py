Employees = {"Names":"Sannihitha","Age":"20","Salary":"50000","Company":"IBM"}
print(type(Employees))
print("printing employee data:")
print(Employees)
Employees['Emp_ages']=[21,23,25]
print("\n Dictionary after adding 3 elements:")
print(Employees)
print("Deleting the employees data 'Company':")
del Employees['Company']
print("printing the modified information:")
print(Employees)
