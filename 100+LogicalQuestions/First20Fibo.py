#35.Print the first 20 numbers of a Fibonacci series
def fibonacci_series(n):
    a, b = 0, 1  # Starting values of the Fibonacci series
    for i in range(n):
        print(a, end=" ")  # Print the current Fibonacci number
        a, b = b, a + b  # Update a and b to the next two numbers in the series

# Print the first 20 Fibonacci numbers
fibonacci_series(20)
