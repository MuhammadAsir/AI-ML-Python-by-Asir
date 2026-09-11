import numpy as np

arr=np.array([1,2,3,4,5,6])

slice_arr = arr[1:4]
slice_arr[0] = 100
print("Original:", arr)
print("Slice:", slice_arr,'\n')  #Changing view → changes original

"""Why did original array change?Because:
NumPy slicing creates a VIEW, not a copy. So both arrays share the same memory."""

arr2 = np.array([1, 2, 3, 4, 5])

copy_arr2 = arr2[1:4].copy() #.copy() → creates independent array

copy_arr2[0] = 100

print("Original:", arr2)
print("Copy:", copy_arr2,'\n')
#Now original array is safe! Changing copy → does NOT change original

#advance indexing

lst=np.array([10,20,30,40,50,60])
val=lst[[2,3]] # it will take the index 2 and 3 value which is 30 and 40
print(val) 

#iteration
arr3=np.array([[1,2,4],
               [4,5,6],
               [7,8,9]])

for i in np.nditer(arr3):
    print(i)



