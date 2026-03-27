import pandas as pd

# Read Excel file

df = pd.read_excel(r"C:\Users\HP\Downloads\employee.xlsx")
print(df)

# a) Employees in Automotive domain
print("Automotive Employees:")
print(df[df["Department"] == "Automotive"])

# b) Employee details by ID
emp_id = int(input("Enter Employee ID: "))
print("\nEmployee Details:")
print(df[df["Employee ID"] == emp_id])

# d) Developers list
print("\nDevelopers:")
print(df[df["Designation"] == "Developer"])