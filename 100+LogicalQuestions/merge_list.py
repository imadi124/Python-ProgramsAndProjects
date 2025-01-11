#68.	Write a program to merge 2 list without using the + operator

list1 = [1,2,3,4,5,6,7,8]
list2 = [10,9,8,7,6,5,4,3,2,1]
result_list = []

for i in list1:
    result_list.append(i)

for i in list2:
    result_list.append(i)

print(f"The merged list is {result_list}")

sorted_list = sorted(result_list)
print(f"The sorted merged list is :{sorted_list}")