#36.Write a program to find the compound interest 

def compound_interest(principal, rate, time):
    amount = principal * (1 + rate / 100) ** time
    # Calculate the compound interest
    ci = amount - principal
    return ci

# Input from the user
principal = float(input("Enter the principal amount: "))
rate = float(input("Enter the rate of interest (in percentage): "))
time = float(input("Enter the time (in years): "))

# Calculate and print the compound interest
ci = compound_interest(principal, rate, time)
print(f"The compound interest is: {ci:.2f}")
