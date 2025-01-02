#1.	User will input (3ages).Find the oldest one
age1 = int(input("Enter first age "))
age2 = int(input("Enter second age "))
age3 = int(input("Enter third age "))
oldest = max(age1, age2, age3)
print(f"The oldest age is {oldest}")