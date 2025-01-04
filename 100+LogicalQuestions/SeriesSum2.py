"""47.	Write a Python Program to Find the Sum of the Series till the nth term: 
1 + x^2/2 + x^3/3 + … x^n/n
n will be provided by the user
"""

x = float(input("Enter the value of x: "))
n = int(input("Enter the number of terms (n): "))

if n <= 0:
    print("Please enter a valid positive integer for n.")
else:

    series_sum = 1  
    
    for i in range(2, n + 1): 
        term = (x ** i) / i 
        series_sum += term  
    
    print(f"The sum of the series up to {n} terms is: {series_sum}")
