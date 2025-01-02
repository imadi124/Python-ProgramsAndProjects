# 18.Write a program that will check whether the number is armstrong number or not.
# Function to check if a number is Armstrong
def is_armstrong(num):
    # Convert the number to string to get the number of digits
    num_str = str(num)
    num_digits = len(num_str)
    
    sum_of_powers = sum(int(digit)**num_digits for digit in num_str)
    
    # Check if the sum equals the original number
    if sum_of_powers == num:
        return True
    else:
        return False

# Taking input from the user
num = int(input("Enter a number to check if it is an Armstrong number: "))

# Checking if the number is Armstrong
if is_armstrong(num):
    print(f"{num} is an Armstrong number.")
else:
    print(f"{num} is not an Armstrong number.")




























