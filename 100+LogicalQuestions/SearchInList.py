my_list = []
while True :
    print("Enter number to add in the list (Type 'done' to exit) :")
    user_input = input().strip()

    if user_input == 'done' :
        break

    try:
        num = int(user_input)
        my_list.append(num)
    except ValueError:
        print("Invalid input . Please enter a number or 'done' to finish.")


print("Your list :" , my_list)

search_num = int(input("Enter the number to search in the list :"))

if search_num in my_list:
    print(f"{search_num} is found in the list.")

else:
    print(f"{search_num} is not found in the list.")