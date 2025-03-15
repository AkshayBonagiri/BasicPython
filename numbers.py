# Get the number from the user
number = int(input("Enter a number: "))

# Check the sign and parity of the number
if number > 0 and number % 2 == 0:
    print(number, "is positive and even")
elif number < 0 and number % 2 == 0:
    print(number, "is negative and even")
elif number > 0 and number % 2 != 0:
    print(number, "is positive and odd")
else:
    print(number, "is negative and odd")
