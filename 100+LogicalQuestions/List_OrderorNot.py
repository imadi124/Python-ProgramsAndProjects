#66.Write a program to check if a list is in ascending order or not

user_input = input("Enter numbers separated by spaces to create a list: ")

my_list = list(map(int, user_input.split()))

# Check if the list is in ascending order
is_ascending = True  # Assume the list is ascending
for i in range(len(my_list) - 1):  # range(len(my_list) - 1) because for my_list[i] > my_list[i + 1]
    if my_list[i] > my_list[i + 1]:  # Check if the current element is greater than the next
        is_ascending = False 
        break 

if is_ascending:
    print("The list is in ascending order.")
else:
    print("The list is not in ascending order.")
