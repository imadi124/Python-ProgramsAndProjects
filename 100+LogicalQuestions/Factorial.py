#26.Write a program that can find the factorial of a given number provided by the user.

num = int(input("enter a number to find the factorial :"))
factorial = 1 
if num < 0:
    print("Factorial is not defined for negative numbers.")
else:
    for i in range(1,num+1):
        factorial *= i
print(f"The factorial of {num} is : {factorial}")
