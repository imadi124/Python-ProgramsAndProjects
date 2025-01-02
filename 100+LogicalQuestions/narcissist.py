#19.Write a program that will take user input of (4 digits number) and check whether the number is narcissist number or not.

#Narcissistic numbers: A specific term used to describe numbers where
# the sum of each digit raised to the power of the number of digits equals the number itself
#(though it's mostly used interchangeably with Armstrong numbers).

# Function to check if a number is a narcissistic number
def is_narcissistic(num):
    # Convert the number to string to get the number of digits
    num_str = str(num)
    num_digits = len(num_str)
    
    # Calculate the sum of each digit raised to the power of num_digits
    sum_of_powers = sum(int(digit)**num_digits for digit in num_str)
    
    # Check if the sum equals the original number
    if sum_of_powers == num:
        return True
    else:
        return False

# Taking input from the user
num = int(input("Enter a 4-digit number to check if it is a narcissistic number: "))

# Checking if the number is narcissistic
if len(str(num)) == 4:  # Ensures the input is a 4-digit number
    if is_narcissistic(num):
        print(f"{num} is a narcissistic number.")
    else:
        print(f"{num} is not a narcissistic number.")
else:
    print("Please enter a valid 4-digit number.")
