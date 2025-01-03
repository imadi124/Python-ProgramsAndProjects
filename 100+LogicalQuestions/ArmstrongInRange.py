#29.Print all the armstrong numbers in the range of 100 to 1000

def is_armstrong(num):

    num_str = str(num)

    no_of_digits = len(num_str)

    sum_of_powers = sum(int(digit)**no_of_digits for digit in num_str)

    return sum_of_powers == num 

# Loop through the range 100 to 1000
print("Armstrong numbers between 100 and 1000:")
for i in range(100, 1001):  # 1000+1 is 1001
    if is_armstrong(i):  # Call the function with i as argument
        print(i)  # Print the Armstrong number