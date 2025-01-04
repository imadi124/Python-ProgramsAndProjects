# 48. The natural logarithm can be approximated by the following series:
# Series: (x-1)/x + (1/2)((x-1)/x)^2 + (1/2)((x-1)/x)^3 + ... up to the nth term.
# Write a program to calculate the sum of the first seven terms of this series 
# when x is input through the keyboard.

x = float(input("Enter the value of x: "))

# Calculate the first term of the series (common factor)
term = (x - 1) / x  # First term of the series

# Initialize the sum with the first term
series_sum = term

# Loop to calculate and add the next six terms
for i in range(2, 8):  # From the 2nd term to the 7th term
    term = (1 / 2) * (term ** i)  # Calculate the nth term
    series_sum += term  # Add the term to the series sum

# Print the result
print(f"The sum of the first seven terms of the series is: {series_sum}")
