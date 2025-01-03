#39.Print all factors of a given number provided by the user.

num = int(input("Enter a number to check all its factors :"))
# Find and print all factors of the number
print(f"Factors of {num} are:")
for i in range(1, num + 1):
    if num % i == 0:
        print(i)
