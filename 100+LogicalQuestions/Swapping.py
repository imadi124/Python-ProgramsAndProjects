#3.	User will input (2numbers).Write a program to swap the numbers
num1 = int(input("Enter the first number :"))
num2 = int(input("Enter the second number :"))
#Before swapping 
print(f"Before swapping the number num1 = {num1} and num2 = {num2}")
#After swapping 
num1, num2 = num2 , num1 
print(f"After swapping num1= {num1} and num2 = {num2}")