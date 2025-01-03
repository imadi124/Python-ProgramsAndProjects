#21.Write a menu driven program - 1.cm to ft  2.kl to miles  3.usd to inr  4.exit

def cm_to_ft(cm):
    return cm / 30.48

def kl_to_miles(kl):
    return kl * 0.621371

def usd_to_inr(usd):
    return usd * 83.0  # Assuming the exchange rate is 1 USD = 83 INR

while True:
    print("Menu:")
    print("1. Convert cm to ft")
    print("2. Convert kilometers to miles")
    print("3. Convert USD to INR")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        cm = float(input("Enter length in cm: "))
        ft = cm_to_ft(cm)
        print(f"{cm} cm is equal to {ft:.2f} feet")

    elif choice == 2:
        kl = float(input("Enter distance in kilometers: "))
        miles = kl_to_miles(kl)
        print(f"{kl} kilometers is equal to {miles:.2f} miles")

    elif choice == 3:
        usd = float(input("Enter amount in USD: "))
        inr = usd_to_inr(usd)
        print(f"{usd} USD is equal to {inr:.2f} INR")

    elif choice == 4:
        print("Exiting the program...")
        break

    else:
        print("Invalid choice. Please enter a valid option.")

