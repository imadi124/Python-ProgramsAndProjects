#58.Write a python program to remove all the duplicates from a list

# Taking input from the user
user_input = input("Enter the list elements separated by spaces: ")

# Convert the input string to a list of elements
my_list = user_input.split()

# Remove duplicates by converting to a set and back to a list
unique_list = list(set(my_list))

# Print the list after removing duplicates
print("List after removing duplicates:", unique_list)


