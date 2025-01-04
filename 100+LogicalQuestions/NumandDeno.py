# #50.	Write a program that accepts 2 numbers from the user a numerator and a denominator and then simplifies it
# Eg if the num = 5, den = 15 the answer should be ⅓
# Eg if the num = 6, den = 9 the answer should be ⅔
import math

def simplify_fraction(numerator, denominator):
    gcd = math.gcd(numerator, denominator)
    simplified_num = numerator // gcd
    simplified_den = denominator // gcd
    return simplified_num, simplified_den

# Input from the user
numerator = int(input("Enter the numerator: "))
denominator = int(input("Enter the denominator: "))

# Check for zero denominator
if denominator == 0:
    print("Denominator cannot be zero.")
else:
    simplified_num, simplified_den = simplify_fraction(numerator, denominator)
    print(f"The simplified fraction is {simplified_num}/{simplified_den}")
