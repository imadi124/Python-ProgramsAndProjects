#11.	Write a program to find the simple interest when the value of principle,rate of interest and time period is given.
principle = float(input("Enter the principle amount : "))
rate = float(input("Enter the rate : "))
time = float(input("Enter the time in years : "))

Simple_interest = (principle*rate*time)/100

print(f"The simple interest is {Simple_interest:.2f}")