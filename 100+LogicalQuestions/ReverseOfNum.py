#40.Find the reverse of a number provided by the user(any number of digit) 

num = int(input ("Enter a number to reverse :"))
str_num = str(num)[::-1]
print(f"The reverse of {num} is {str_num}")
