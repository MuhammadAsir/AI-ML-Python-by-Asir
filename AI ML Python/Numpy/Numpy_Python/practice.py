import numpy as np
"""
numpy is a library in python which is used for scientific computing and data analysis. 
It provides a powerful array object and a collection of functions for working with arrays.
It is mainly used for numerical computations, data manipulation, and machine learning tasks.

"""

arr2=np.array([[1,2,3],
               [4,5,6],
               [7,8,9]])

#2d=arr[row start:row end : step , col_start:col_end : step]

por=arr2[0:2,::]
por1=arr2[2:,::]
print(por1)

