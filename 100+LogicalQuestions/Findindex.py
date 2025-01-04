#54.Find the index position of a particular character in another string. 

string = input("Enter a String: ")
char = input("Enter the character to search the first index: ")

for index, value in enumerate(string): #index provides the index value while value iterators for character search
    if value == char:
        print(f"The first index of '{char}' is: {index}")
        break  # Exit after finding the first occurrence
