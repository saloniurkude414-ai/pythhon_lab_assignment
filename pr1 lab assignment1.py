# Input employee details
name = input("Enter Employee Name: ")
emp_id = input("Enter Employee ID: ")
department = input("Enter Department: ")
basic_salary = float(input("Enter Basic Salary: "))

# Salary calculations
DA = 0.92 * basic_salary
HRA = 0.58 * basic_salary
TA = 0.30 * basic_salary
LIC = 500

# Gross and Net Salary
gross_salary = basic_salary + DA + HRA + TA
net_salary = gross_salary - LIC

# Display salary details
print("\n--- Employee Salary Details ---")
print("Name:", name)
print("Employee ID:", emp_id)
print("Department:", department)
print("Basic Salary: Rs.", basic_salary)
print("DA: Rs.", DA)
print("HRA: Rs.", HRA)
print("TA: Rs.", TA)
print("LIC Deduction: Rs.", LIC)
print("Net Salary: Rs.", net_salary)
