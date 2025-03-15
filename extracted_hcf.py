# Get input from the user
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

# Find the smaller of the two numbers
min_num = min(num1, num2)

# Initialize HCF to 1 (the minimum possible HCF)
hef = 1

# Loop from 1 to the smaller number
for i in range(1, min_num + 1):

# If both numbers are divisible by i, then i is a common factor
if numl % i == @ and num2 % i ==

hef = i

# Print the HCF
print(f"The HCF of {num1} and {num2} is {hcf}.")
