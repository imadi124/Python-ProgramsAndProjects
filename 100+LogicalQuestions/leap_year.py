# Program to check if a year is a leap year
year = int(input("Enter a year to check if it is a leap year or not: "))

# Check leap year conditions
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("The entered year is a leap year.")
else:
    print("The entered year is not a leap year.")
