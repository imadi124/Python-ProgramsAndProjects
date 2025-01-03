#33.User will provide 2 numbers you have to find the by LCM of those 2 numbers
# Function to find HCF using Euclidean algorithm
def hcf(a, b):
    while b:
        a, b = b, a % b
    return a

# Function to find LCM using the relation between LCM and HCF
def lcm(a, b):
    return abs(a * b) // hcf(a, b)

# Input from the user
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

# Find and print the LCM
result = lcm(num1, num2)
print(f"The LCM of {num1} and {num2} is: {result}")
