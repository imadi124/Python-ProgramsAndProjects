#31.Write a program to print all the unique combinations of 1,2,3 and 4

for i in range(1, 5):
    for j in range(i + 1, 5):  # Start j from i + 1 to avoid repetitions
        print((i, j))
