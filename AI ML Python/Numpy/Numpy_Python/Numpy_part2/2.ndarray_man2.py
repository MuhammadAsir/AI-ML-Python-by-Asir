#Numpy array manipulation 2
import numpy as np 

mat=np.array([[10,20,30],
             [40,50,60],
             [70,80,90]
             ])
print(mat,'\n')
transpose=mat.T
print(transpose,'\n')

#array split
x = np.random.randint(1, 10, size=(10))
print(x)
x_split=np.array_split(x,3) #It will split the data by 3
print(x_split)

# np.split(),Equal splits only
# np.array_split(),Equal and Unequal splits allowed