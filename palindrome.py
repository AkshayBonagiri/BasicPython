# Get the number from the user
number = input("Enter a number: ")

# Check if the number is a palindrome
if number == number[::-1]:
    print("Yes, it's a palindrome.")
else:
    print("No, it's not a palindrome.")
