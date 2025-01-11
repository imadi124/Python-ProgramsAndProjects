# 70.	Write a program that can convert a 2D list to 1D listWrite a program that can print 

two_D_List = [[1,2,3],[4,5,6],[7,8,9]]
one_D_list =[]

for sublist in two_D_List:
    for items in sublist:
        one_D_list.append(items)


print("2D list :",two_D_List)
print("1D list :", one_D_list)