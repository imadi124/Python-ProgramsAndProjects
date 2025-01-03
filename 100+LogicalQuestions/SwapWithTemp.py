#23.Write a program that will swap numbers
num1 = int(input("Enter first number :"))
num2 = int(input("Enter second number :"))
print(f"Before swapping num1 = {num1} and num2 = {num2}")
temp = num1 
num1 = num2 
num2 = temp
print(f"After swapping num1 = {num1} and num2 = {num2}")
