"""46.	Write a program to calculate the sum of the following series till the nth term
1/1! + 2/2! + 3/3! + 4/4! +…….+ n/n!
n will be provided by the user
"""


import math 

n = int(input("Enter a number for the nth term of the series: "))

if n <= 0:
    print("Please enter a valid positive integer.")
else:
    series_sum = 0

    for i in range(1, n + 1):
        series_sum += i / math.factorial(i)

    print(f"The sum of the series up to {n} terms is: {series_sum}")
