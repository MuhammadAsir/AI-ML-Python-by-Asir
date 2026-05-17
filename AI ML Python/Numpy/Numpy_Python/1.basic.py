import numpy as np

# 1d array
arr1=np.array([1,2,3,4,5])
arr1=arr1*5
print(type(arr1))
print(arr1)

print("Dimension",arr1.ndim)# it will tell the dimension

#2d array
print('\n')
arr2=np.array([[1,2,4],
               [4,5,6],
               [7,8,9]]
               )

arr2=arr2*2
print(type(arr2))
print(arr2)
print("Dimension",arr2.ndim,'\n')

#3d array

arr3=np.array([
               [[1,2],[3,4]], #1st floor
               [[5,6],[7,8]], # 2nd floor
               [[9,10],[11,12]] #3rd floor
               ])
print(type(arr3))
print(arr3)
print("Dimension",arr3.ndim,'\n')


#upcasting
arr4=np.array([1,2,3.0])
print(arr4.dtype) # upcasted to float data type
arr5=np.array([1,2,3.2,'4'])
print(arr5.dtype,'\n') # upcasted to string data type

#shape
print("Shape",arr1.shape) # for 1d array there will be no column and row
print("Shape",arr2.shape)
print("Shape",arr3.shape)

#data type

print("Shape",arr1.dtype)
print("Shape",arr2.dtype)
print("Shape",arr3.dtype)

#Size

print("Shape",arr1.size)
print("Shape",arr2.size)
print("Shape",arr3.size)



