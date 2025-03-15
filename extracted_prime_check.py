# Get input from the user
num = int(input("Enter a number: "))

# Assume the number is prime
is_prime = True

# A prime number is greater than 1
if num <= 1:
is_prime = False
else:
# Check for factors from 2 to the square root of the number
for i in range(2, int (nun ** 9.5) +1):
if num % i == @:
is_prime = False
break

# Print the result
if is_prime:

print(f"{num} is a prime number.")
else:

print(f"{num} is not a prime number.")
