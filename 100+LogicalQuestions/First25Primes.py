# Function to check if a number is prime
def is_prime(num):
    if num<2:
        return False 
    for i in range(2,int(num**0.5)+1):
        if num % i == 0:
            return False 
    return True

count = 0
num = 2 

while count<25:
    if is_prime(num):
        print(num , end = " ")
        count += 1

    num += 1


