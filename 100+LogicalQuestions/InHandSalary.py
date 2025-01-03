#20.Write a program that will give you the in hand salary after deduction of HRA(10%),DA(5%),PF(3%), 
# and tax(if salary is between 5-10 lakh–10%),(11-20lakh–20%),(20< _   – 30%)(0-1lakh print k).

# Deduction percentages
HRA = 10 / 100
DA = 5 / 100
PF = 3 / 100

# Input the salary
CTC = int(input("Enter your salary to check in-hand salary: "))

# Check salary ranges and calculate deductions
if CTC <= 100000:
    print("Salary is below 1 Lakh, can't calculate.")
elif CTC >= 500000 and CTC <= 1000000:
    tax = 10 / 100  # Tax rate for salary between 5-10 lakh
elif CTC >= 1000000 and CTC <= 2000000:
    tax = 20 / 100  # Tax rate for salary between 11-20 lakh
elif CTC > 2000000:
    tax = 30 / 100  # Tax rate for salary above 20 lakh
else:
    print("Invalid Salary Range")
    tax = 0

# Calculate deductions
hra = CTC * HRA
da = CTC * DA
pf = CTC * PF
tax_deduction = CTC * tax

# Calculate in-hand salary
in_hand_salary = CTC - (hra + da + pf + tax_deduction)

# Output the result
print(f"In-hand Salary after deductions: {in_hand_salary}")
