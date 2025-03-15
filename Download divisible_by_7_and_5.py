# Loop through the range from 1200 to 2200
for num in range(1200, 2201):
    # Check if the number is divisible by 7 and a multiple of 5
    if num % 7 == 0 and num % 5 == 0:
        print(num)
