#65.Write a program that can count the number of words in a given string

string = input("Enter a string :")
words = string.split()
length = len(words)
print(f"Number of words in the string entered is : {length}")
