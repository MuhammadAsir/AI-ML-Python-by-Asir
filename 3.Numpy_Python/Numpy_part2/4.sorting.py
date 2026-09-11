import numpy as np  

#Inplace sorting

x=np.array([10, 5, 3, 8, 2])

z=x.copy() #To create a copy of x and sort it without affecting x

z.sort() #This will sort the array z in place
print("Original array:", x)
print("Sorted array:", z)

print('\n')
#Copy sorting

copy_sort=np.sort(x) #This will return a sorted copy of x without affecting x
print("Sorted array using np.sort:", copy_sort)
print("Original array:", x)

#2d array sorting
y=np.array([[10,12,9], [6, 5, 4]])
print("Original 2D array:\n", y)
horizontal_sort=np.sort(y,axis=1)
print("Horizontal sort:\n", horizontal_sort)
vertical_sort=np.sort(y,axis=0)
print("Vertical sort:\n", vertical_sort)    