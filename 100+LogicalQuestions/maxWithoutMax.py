#60.Write a python program to find the max item from a list without using the max function
def find_max(item_list):
    max_item = item_list[0]  # Assume the first item is the max

    for item in item_list:
        if item > max_item:
            max_item = item

    return max_item

item_list = []

# Start taking inputs
while True:
    numbers = input("Enter a number (or type 'Done' to finish): ")
    
    if numbers.lower() == "done":
        break
    
    # Convert the input to an integer and add it to the list
    item_list.append(int(numbers))

# Call the function to find the maximum value
if item_list:  # Check if the list is not empty
    result = find_max(item_list)
    print("The maximum item is:", result)
else:
    print("No numbers were entered.")
