
import numpy as np

x = np.random.randint(1, 100, size=(100))

val_greater_than_50 = np.count_nonzero(x > 50)
print(val_greater_than_50)

#Unique value

unique_val=np.unique(x) 
print(unique_val)

unique_val_count=np.unique(x,return_counts=True)
print(unique_val_count)
"""It will return a tuple of two arrays, 
the first array contains the unique values and 
the second array contains the count of each unique value in the original array."""