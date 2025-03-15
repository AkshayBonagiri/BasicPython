# Initialize variables to store the total temperature
total_temp = 0

# Input temperatures for each day of the week
for day in range(1, 8):
    temp = float(input(f"Enter the temperature for day {day}: "))
    total_temp = total_temp + temp

# Calculate the average temperature
average_temp = total_temp / 7

# Display the average temperature
print("The average temperature for the week is:", average_temp, "°C")
