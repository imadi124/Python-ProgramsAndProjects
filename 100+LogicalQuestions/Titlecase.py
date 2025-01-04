#59.Write a python program to convert a string to title case without using the title()

string = input("Enter a string to convert it to title case :")

words = string.split()

title_case_string = ' '.join([word.capitalize() for word in words])

print(f"The title for the given input is : {title_case_string}")