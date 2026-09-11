import numpy as np  

arr1=np.array([1,2,3,4,5],dtype=np.int8) #changing the datatype into int8
print(arr1.dtype)
 # int8 range is -127 to 128, so if we store [1,2,300],it will show error

arr2 = np.array([1, True, 3.23, 'hello'])
print(arr2.dtype)
#it will convert it into string
"""
NumPy arrays must have one single data type (dtype).
If you mix types (int, float, string), NumPy converts everything to a common type
"""
