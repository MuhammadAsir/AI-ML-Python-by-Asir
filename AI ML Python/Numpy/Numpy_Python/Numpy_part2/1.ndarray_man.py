#Numpy array manipulation
import numpy as np

arr = np.random.randint(1, 100, size=(10, 5))

print("Original Array:\n", arr)
print("Shape:", arr.shape)   # (10, 5)
print("Dimension:", arr.ndim, '\n')

#Reshape the array to (5, 10)
b = np.reshape(arr, (5, 10))

print("Reshaped Array (5,10):\n", b)
print("Shape:", b.shape)   # (5, 10)
print("Dimension:", b.ndim, '\n')

"""
Explanation:
10 * 5 = 50 → total elements = 50
So we can reshape into any size where:
rows * columns = 50
Valid examples:
5 * 10 = 50
25 * 2 = 50
Invalid example:
3 * 5 = 15 ❌ (not equal to 50, so not possible)
"""

#Column-wise Flatten 
flat_col = np.ravel(arr, order='F')

print("Column-wise Flatten (F-order):\n", flat_col)
print("Shape:", flat_col.shape)
print("Dimension:", flat_col.ndim, '\n')

#Column-wise Flatten 
flat_row = np.ravel(arr, order='C')

print("Column-wise Flatten (C-order):\n", flat_row)
print("Shape:", flat_row.shape)
print("Dimension:", flat_row.ndim, '\n')
"""
Example:
[[1, 2],
 [3, 4]]

Row-wise  → [1, 2, 3, 4]
Column-wise → [1, 3, 2, 4]
"""

#Concatenate
x = np.random.randint(1, 10, size=(2, 3))
y = np.random.randint(11, 20, size=(2, 3))
print(x,'\n')
print(y,'\n')


row_cat=np.concatenate((x,y),axis=0) #Number of columns must be SAME for row wise concatenate
print(row_cat,'\n')

col_cat=np.concatenate((x,y),axis=1) #Number of rows must be SAME for column wise concatenate
print(col_cat,'\n')

