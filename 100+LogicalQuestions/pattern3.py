'''
43.	Write  a program to print the following pattern
        *
      * * *
    * * * * *
   * * * * * * *
* * * * * * * * *
'''
rows = 5
for i in range(rows):
    # Calculate the number of stars for the current row
    stars = 2 * i + 1
    # Calculate spaces for center alignment
    spaces = rows - i - 1
    # Print spaces and stars
    print(" " * spaces + "*" * stars)
