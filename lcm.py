# Get input from the user
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

# Find the greater of the two numbers
greater = max(num1, num2)

# Start from the greater number and find the LCM
while True:
    if greater % num1 == 0 and greater % num2 == 0:
        lcm = greater
        break
    greater += 1

# Print the LCM
print(f"The LCM of {num1} and {num2} is {lcm}.")
