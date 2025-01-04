#55.Count the number of vowels in a string provided by the user.
string = input("Enter a string: ")
vowels = ['a', 'e', 'i', 'o', 'u']
count = 0

# Convert the string to lowercase to handle both uppercase and lowercase vowels
string = string.lower()

for char in string:
    if char in vowels:
        count += 1

print(f"The number of vowels in the string is: {count}")
