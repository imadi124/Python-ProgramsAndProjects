#12.Write a program to find the volume of the cylinder. Also find the cost when ,when the cost of 1litre milk is 40Rs.
# Program to calculate the volume of a cylinder and the cost of milk

# Inputs for radius and height
radius = float(input("Enter the radius of the cylinder (in cm): "))
height = float(input("Enter the height of the cylinder (in cm): "))

# Calculate the volume (in cubic centimeters)
volume_cm3 = 3.14 * (radius ** 2) * height

# Convert volume to liters (1 liter = 1000 cm³)
volume_liters = volume_cm3 / 1000

# Calculate the cost (cost of 1 liter of milk is Rs. 40)
cost = volume_liters * 40

# Display the results
print(f"The volume of the cylinder is {volume_liters:.2f} liters.")
print(f"The cost of {volume_liters:.2f} liters of milk is Rs. {cost:.2f}")
