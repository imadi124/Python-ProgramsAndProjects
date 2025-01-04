#57.Write a program that can check whether a given string is palindrome or not.

string = input("Enter a String :")
reverse = string[::-1]
if string == reverse :
    print("Palindrome")
else:
    print("Not palindrome.")
