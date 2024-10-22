#Basic calculator python project
def add(x, y):
    return x + y


def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    return x / y



def modulus(x, y):
    return x % y



def exponentiate(x, y):
    return x ** y



def calculator():
    while True:
        print("\nBasic Python Calculator")
        print("Select operation:")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Modulus")
        print("6. Exponentiation")
        print("7. Exit")

        
        
        choice = input("Enter choice (1/2/3/4/5/6/7): ")

        if choice == '7':
            print("Exiting the calculator. Goodbye!")
            break

      
      
        if choice not in ['1', '2', '3', '4', '5', '6']:
            print("Invalid Input. Please choose a valid option.")
            continue

        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            if choice == '1':
                print(f"{num1} + {num2} = {add(num1, num2)}")
            elif choice == '2':
                print(f"{num1} - {num2} = {subtract(num1, num2)}")
            elif choice == '3':
                print(f"{num1} * {num2} = {multiply(num1, num2)}")
            elif choice == '4':
                print(f"{num1} / {num2} = {divide(num1, num2)}")
            elif choice == '5':
                print(f"{num1} % {num2} = {modulus(num1, num2)}")
            elif choice == '6':
                print(f"{num1} ^ {num2} = {exponentiate(num1, num2)}")

        except ValueError:
            print("Invalid input! Please enter a valid number.")
calculator()
