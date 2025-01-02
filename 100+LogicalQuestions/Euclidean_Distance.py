#8.	Write a program to find the euclidean distance between two coordinates.
import math
x1 , y1 = map(float,input("Enter the coordinates of the first point(x1 , y1 ):").split())
x2 , y2 = map(float,input("Enter the coordinates of the first point(x2 , y2 ):").split())
euclidean_distance = math.sqrt((x2-x1)**2 + (y2-y1)**2)
print(f"The Euclidean distance for the corrdinates {x1 , y1} and {x2 , y2} is {euclidean_distance:.2f}")