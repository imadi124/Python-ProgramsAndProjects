try:
    # Input from the user
    num = int(input("Enter a number: "))
    
    # Check if the number is less than 2
    if num < 2:
        print(f"{num} is not a prime number.")
    else:
        # Assume the number is prime
        is_prime = True

        # Check for factors from 2 to sqrt(num)
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                is_prime = False
                break

        # Output the result
        if is_prime:
            print(f"{num} is a prime number.")
        else:
            print(f"{num} is not a prime number.")
except ValueError:
    print("Invalid input! Please enter an integer.")
