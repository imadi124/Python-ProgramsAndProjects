#37.Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn.

n = int(input("Enter a number : "))
result = n+(n*n)+(n*n*n)
print(f"Value of n+nn+nnn for {n} is {result}")