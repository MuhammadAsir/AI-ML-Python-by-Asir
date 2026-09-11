import numpy as np  


x = np.random.randint(11, 20, size=(2, 2))
y= np.random.randint(1, 10, size=(2, 2))

add=x+y
print(x,y,add,sep="\n\n")

sub=x-y
print(sub,'\n')

remainder=x%y
print(remainder,'\n')

#Trigonometric functions

sin_val=np.sin(x) #In radian values
print(sin_val,'\n')
cos_val=np.cos(x)  
print(cos_val,'\n')

#Radian to degree 
deg_conversion=np.rad2deg(x)
print(deg_conversion,'\n')
#If i want to convert degree to radian then we can use deg2rad function

#Logarithmic functions

log10_val=np.log10(x)
print("Log10 value",log10_val,'\n')
log2_val=np.log2(x)
print("Log2 value",log2_val,'\n')

#Square root
square_root=np.sqrt(x)
print("Square root",square_root,'\n')

#Sum
sum_val=np.sum(x)
print("Sum of all elements",sum_val,'\n')
cumulative_sum=np.cumsum(x)
print("Cumulative sum",cumulative_sum,'\n')
