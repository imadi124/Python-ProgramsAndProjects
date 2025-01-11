
my_list1 = [1, 54, 6, 23, 67, 58, 12, 2, 54]
my_list2 = [1, 2, 3, 4, 6, 7, 8, 9, 10]

union = list(set(my_list1) | set(my_list2))

intersection = list(set(my_list1) & set(my_list2))  

# Print results
print(f"The union of both lists is: {union}")
print(f"The intersection of both lists is: {intersection}")
