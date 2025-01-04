'''
45.	Write a program to print the following pattern
1
2 3
4 5 6
7 8 9 10
'''

current = 1 
for i in range(1 , 5):
    for j in range(i):
        print(current  , end =" ")
        current += 1
    print()