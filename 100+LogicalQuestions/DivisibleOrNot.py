# Program to check if a number is divisible by both 3 and 6
num = int(input("Enter the number to check if it is divisible by both 3 and 6: "))

# Check divisibility
if num % 3 == 0 and num % 6 == 0:
    print("The number is divisible by both 3 and 6.")
else:
    print("The number is not divisible by both 3 and 6.")
