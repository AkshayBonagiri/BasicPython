# Get the dimensions of the cuboid from the user
length = float(input("Enter the length of the cuboid: "))
width = float(input("Enter the width of the cuboid: "))
height = float(input("Enter the height of the cuboid: "))

# Calculate the volume of the cuboid
volume = length * width * height

# Calculate the surface area of the cuboid
surface_area = 2 * (length * width + width * height + height * length)

# Print the results
print("Volume of the cuboid:", volume)
print(f"Surface area of the cuboid:", surface_area)
