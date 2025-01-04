#53.Count the frequency of a particular character in a provided string. Eg 'hello how are you' is the string, the frequency of h in this string is 2.
string = input("Enter a string: ")
x = input("Enter the character to count the frequency inside the string: ")

count = 0
for char in string:
    if char == x:
        count += 1

print(f"The frequency of '{x}' in '{string}' is: {count}")
