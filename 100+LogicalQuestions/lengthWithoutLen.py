#51.Find the length of a given string without using the len() function. 
string = input("Enter a string: ")
count = 0

for char in string:
    count += 1

print(f"The length of the string is: {count}")
