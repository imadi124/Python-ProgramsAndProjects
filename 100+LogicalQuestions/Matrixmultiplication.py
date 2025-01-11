
matrix1 = [[1, 2, 3], [4, 5, 6], [0, 9, 8]]
matrix2 = [[34, 2, 75], [5, 2, 5]]

rows1 = len(matrix1)  #Rows in matrix 1 
cols1 = len(matrix1[0]) if rows1 > 0 else 0  #Columns in matrix 1 
rows2 = len(matrix2)  #Rows in matrix 2 
cols2 = len(matrix2[0]) if rows2 > 0 else 0 #Columns in matrix 2

# Check if multiplication is possible
if cols1 == rows2:
    print("Matrix Multiplication is possible")
    print(f"Resultant matrix shape will be: {rows1} x {cols2}")
else:
    print("Matrix Multiplication is not possible")
