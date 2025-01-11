#74.	Write a program to print the shape of a matrix. 

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [10, 11, 12]
]


rows = len(matrix)  
cols = len(matrix[0]) if rows > 0 else 0 

print(f"The shape of the matrix is: {rows} x {cols}")
