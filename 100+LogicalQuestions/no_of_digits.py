#Take a number from the user and find the number of digits in it. 

num = int(input("Enter a number to check the number of digits :"))
str_num = str(num)
print(f"The number of digits in the entered number {num} is {len(str_num)}")