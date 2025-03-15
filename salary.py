# Get the employee's details from the user
name = input("Enter the employee's name: ")
age = int(input("Enter the employee's age: "))
basic_salary = float(input("Enter the employee's basic salary: "))

# Calculate the Dearness Allowance (DA) as 10% of the basic salary
da = 0.10 * basic_salary

# Calculate the House Rent Allowance (HRA) as 10% of the basic salary
hra = 0.10 * basic_salary

# Calculate the total salary
total_salary = basic_salary + da + hra

# Print the employee's details and total salary
print("Employee Name:", name)
print("Employee Age:", age)
print("Basic Salary:", basic_salary)
print("Dearness Allowance (DA):", da)
print("House Rent Allowance (HRA):", hra)
print("Total Salary:", total_salary)
