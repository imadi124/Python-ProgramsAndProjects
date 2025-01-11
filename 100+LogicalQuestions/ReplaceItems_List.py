#69.	Write a program to replace an item with a different item if found in the list 

my_list = ['Apple',"mango","banana","guava","Salad"]

for i in range(len(my_list)):
    if my_list[i].lower() == "salad":
        my_list[i] = "A fruit"
        break


print(my_list)
