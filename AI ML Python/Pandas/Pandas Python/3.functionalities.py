import pandas as pd 
import numpy as np

df=pd.read_csv('student_data.csv')


#First 4 value
print(df.head(4))

# Some final values 
print(df.tail())

#columns 
df.columns 
columns=np.array(df.columns)
print(columns)# converting to array for better visualization
print(columns.dtype) #It means the data type of the columns is object which is a string in pandas

#index
index=np.array(df.index)    
print(index) # it is the row number of the data frame
print(index.dtype) # it is int64 because it is a number

#Info for the data frame
print(df.info()) 
#it gives us the information about the data frame like number of rows, columns, data types and memory usage

print(df.sample(10)) # it gives us random 10 rows from the data frame

#Statisticals summary of the data frame
print(df.describe()) 
#it gives us the statistical summary of the data frame like count, mean, std, min, 25%, 50%, 75% and max values for each column
