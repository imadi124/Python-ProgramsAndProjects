#25.Write a program that can multiply 2 numbers provided by the user without using the * operator


num1 = int(input("Enter first number :"))
num2 = int(input("Enter second number :"))

result = 0 
negative = False 


if num1 < 0:
    num1 = -num1
    negative = not negative

if num2 < 0:
    num2 = -num2
    negative = not negative 

for i in range(num2):
    result+=num1 

if negative:
    result = -result

print(f"The result of multiplying the numbers is: {result}")


