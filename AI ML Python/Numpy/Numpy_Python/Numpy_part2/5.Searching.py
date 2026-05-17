import numpy as np 

# Searching Arrays
x=np.array([1,2,3,4,5,6,7,8,9])

index=np.where(x==5)
print(index,'\n')

ind2=np.where(x%2==0)
print(ind2,'\n')

ind3=np.where(x%2==0,x,0)  #where(condition, value if true, value if false)
#It means if the condition is true then it will return the value otherwise it will return 0
print(ind3,'\n')

mat=np.array([[10,3,5],[8,4,9]])
ind4=np.where(mat>8)
print(ind4,'\n')
#So it means that the value 10 is at index (0,0) and the value 9 is at index (1,2)

ind5=np.argmax(mat) #It will return the index of the maximum value in the array
print("Max number is in index:",ind5,'\n')
