import numpy as np
#np.arange(first,end,step)

arr=np.arange(1,10,1)
print(arr)
print("Shape",arr.shape)
print("Data type",arr.dtype)
print("Size",arr.size,'\n')


arr1=np.arange(1,10,1).reshape(3,3) #reshape will create matrix
print(arr1)
print("Shape",arr1.shape)
print("Data type",arr1.dtype)
print("Size",arr1.size,'\n')

#np.linspace(start,end,point)

arr2=np.linspace(1,10,15) 
print(arr2)
print("Shape",arr2.shape)
print("Data type",arr2.dtype)
print("Size",arr2.size,'\n')

#np.logspace(start,end,point)
arr3=np.logspace(0,4,6) #i can also tell the base: np.logspace(0,4,5,base=2)
print(arr3)
print("Shape",arr3.shape)
print("Data type",arr3.dtype)
print("Size",arr3.size,'\n')