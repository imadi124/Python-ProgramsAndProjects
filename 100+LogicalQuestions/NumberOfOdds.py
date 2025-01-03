#27.Write a program to print the first 25 odd numbers

# Initialize a counter
count = 0
# Initialize the current number to check for odd numbers
current_number = 1

# Loop until 25 odd numbers are printed
while count < 25:
    if current_number % 2 != 0:  # Check if the number is odd
        print(current_number, end= "\n")  # Print the odd number
        count += 1  # Increment the count of odd numbers
    current_number += 1  # Move to the next number
