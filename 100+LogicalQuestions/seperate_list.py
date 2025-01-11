#67.	
# Create 2 lists from a given list,
#  where 1st list will contain all the odd numbers from the original list
#  and the 2nd one will contain all the even numbers 

my_list = [1,2,3,4,5,6,7,8,9,10,11]
odd_list = []
even_list = []
for i in my_list:
     if i % 2 == 0:
        even_list.append(i)

     else :
        odd_list.append(i)


print(f"The list of even number is {even_list}")
print(f"The list of odd numbers is {odd_list}")
        