# Initialize an empty list
my_list = []

# Input numbers into the list
while True:
    print("Enter number to add to the list (Type 'done' to exit):")
    user_input = input().strip()

    # Exit condition
    if user_input.lower() == 'done':
        break

    # Add number to the list after validation
    try:
        num = int(user_input)
        my_list.append(num)
    except ValueError:
        print("Invalid input. Please enter a valid number.")

print(f"Your list: {my_list}")

# Create a new list with squares of the items in the old list
squared_list = [i ** 2 for i in my_list]

print(f"List of squares: {squared_list}")
