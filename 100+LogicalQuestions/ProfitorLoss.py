#10.	Write a program that will take user input of cost price and selling price and determines whether its a loss or a profit
cost = float(input("Enter the cost price :"))
selling_price = float(input("Enter the selling price :"))
if(cost > selling_price):
    print(f"Profit of {cost-selling_price}")
else:
    print(f"loss of {selling_price - cost}")