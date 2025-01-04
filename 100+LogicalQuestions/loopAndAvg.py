# Program to calculate the sum and average of numbers until the user enters 0

SumOfNum = 0 
count = 0     

while True:  
    x = int(input("Enter the number to calculate sum and average (Enter 0 to stop): "))
    
    if x == 0:  
        break   
    
    SumOfNum += x  # Add the number to the sum
    count += 1     # Increment the count

# Calculate the average if at least one number was entered
if count > 0:
    Average = SumOfNum / count
    print(f"Sum of all numbers: {SumOfNum}")
    print(f"Average of all numbers: {Average}")
else:
    print("No numbers were entered.")
