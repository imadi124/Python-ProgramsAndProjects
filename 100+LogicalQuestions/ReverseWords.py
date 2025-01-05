# #64.	Write a program that can reverse words of a given string.
# Eg if the input is Hello how are you
# Output should be you are how Hello

string = input("Enter a string: ")


words = string.split()  # Split the string into a list of words
reversed_words = words[::-1]  # Reverse the list of words
reversed_string = ' '.join(reversed_words)  # Join the words back into a string

# Output the results
print(f"Your string: {string}")
print(f"Reversed words: {reversed_string}")
