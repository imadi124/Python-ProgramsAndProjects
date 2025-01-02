num = int(input("Enter a 4-digit number: "))

# Reverse the number
reverse = int(str(num)[::-1])  # Reverse as string, then convert back to int
print(f"The reverse of the entered number is {reverse}")

# Check if it is a palindrome or not
if num == reverse:
    print("The entered number is a palindrome")
else:
    print("The entered number is not a palindrome")
