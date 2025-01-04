'''
44.	Write a program to print the following pattern
1
1 2 1
1 2 3 2 1
1 2 3 4 3 2 1
1 2 3 4 5 4 3 2 1

'''
rows = 5  # Number of rows
for i in range(1, rows + 1):
    # Generate the ascending sequence
    ascending = list(range(1, i + 1))
    # Generate the descending sequence
    descending = list(range(i - 1, 0, -1))
    # Combine and print the row
    print(" ".join(map(str, ascending + descending)))
