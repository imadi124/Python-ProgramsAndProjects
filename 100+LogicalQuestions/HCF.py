#32.User will provide 2 numbers you have to find the HCF of those 2 numbers
# Input from the user
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

# Function to find HCF using Euclidean algorithm
def hcf(a, b):
    while b:
        a, b = b, a % b
    return a

# Call the function and print the result
result = hcf(num1, num2)
print(f"The HCF of {num1} and {num2} is: {result}")
