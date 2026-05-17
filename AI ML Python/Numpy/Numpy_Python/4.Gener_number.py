#Generating random number

import numpy as np


arr=np.random.rand(2,3) # 0 to 1 value, column 2 row 3
print(arr)
print("Shape",arr.shape)
print("Data type",arr.dtype)
print("Size",arr.size,'\n')

#random integer
#arr1=np.random.randint(start,end,shape)
arr1=np.random.randint(1,10,(2,3)) #integer value 1-10, row2 and column3
print(arr1)
print("Shape",arr1.shape)
print("Data type",arr1.dtype)
print("Size",arr1.size,'\n')

#uniform
arr2=np.random.uniform(1,10,(2,3)) # floating value 1-10, row2 and column3
print(arr2)
print("Shape",arr2.shape)
print("Data type",arr2.dtype)
print("Size",arr2.size,'\n')