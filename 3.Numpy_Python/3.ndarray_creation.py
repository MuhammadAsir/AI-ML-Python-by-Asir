import numpy as np 

#list to np array
lst=[1,2,3,4,5]

arr=np.array(lst) 
print(arr)

mixed_lst=[True,1,2.5,'hello']

arr2=np.array(mixed_lst)
print(arr2)
print(arr2.dtype)

#tuple to np array

tpl=(10,20,30,40)
arr3=np.array(tpl)
print(arr3,'\n')

#set to np array
SET={1,2,3,4}
arr4=np.array(SET) # set → may become object dtype
print(arr4,'\n',arr4.dtype) 
"""
A set is unordered, so NumPy cannot guarantee a consistent numeric structure
 and falls back to storing elements as generic Python objects (dtype=object).
 """



dc={'roll':'123','age':24}
keys=dc.keys()
values=dc.values()

print(keys,values)
items=dc.items()
print(items,'\n')

#keys to ndarray
arr5=np.array(list(keys))
print(arr5)
print('\n')
#items to ndarray

arr6=np.array(list(items))
print(arr6)
print(arr6.dtype)
print(arr6.shape)
print(arr6.size)
