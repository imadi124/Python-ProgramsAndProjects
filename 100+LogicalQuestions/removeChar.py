#56.Write a program which can remove a particular character from a string. 
string = input('Enter a string: ')
x = input("Enter a character to remove from the string: ")

# Remove the character from the string
string = string.replace(x, '')

print("Entered character removed.")
print("Updated string:", string)
