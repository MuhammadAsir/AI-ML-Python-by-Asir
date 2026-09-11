import numpy as np

#np.zeros
arr=np.zeros((3,3))
print(arr)

print('\n')

arr1=np.zeros_like(arr) 
print(arr1)
print('\n')

#np.ones
arr2=np.ones((2,3))
print(arr2)
print('\n')

#empty
arr3 = np.empty((4,3),dtype=np.int8) #it will show random value
print(arr3)
print('\n')

#full
arr4=np.full((3,4),10)#fill with 10
print(arr4,'\n')

#infinity
arr5=np.full((3,3),np.inf)
print(arr5)