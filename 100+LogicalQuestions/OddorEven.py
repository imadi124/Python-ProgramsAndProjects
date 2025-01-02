#6.	Write a program that will tell whether the number entered by the user is odd or even.
num = int(input("Enter the number to check if the number is odd or even :"))
if (num == 0):
    print("The entered number is zero. ")
elif(num%2 == 0):
    print("The entered number is even. ")
else:
    print("The entered number is odd.")