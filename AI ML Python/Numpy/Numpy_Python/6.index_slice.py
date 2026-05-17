import numpy as np

#indexing
arr=np.array([[1,2,4],
               [4,5,6],
               [7,8,9]])

print(arr[2][2])
print(arr[1])

#slicing: 1d=arr[start:end:step]
arr1=np.array([1,2,3,4,5,6,7,8,9,10])
arr_mod=arr1[1:4]
print(arr_mod) #[2,3,4]

# 2d=arr[row start:row end : step , col_start:col_end : step]

arr2=np.array([[1,2,3],
               [4,5,6],
               [7,8,9]])

row0=arr2[0:1,]
print("row 0",row0)
row1=arr2[1:,]
print("row 1",row1)

col0=arr2[ :: , 0:1]
print("col 0",col0)
col1=arr2[ :: , 1:]
print("col 1",col1)

#getting portion

portion=arr2[:: , 0:2]
print(portion)