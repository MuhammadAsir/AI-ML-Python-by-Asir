#Changing index and columns and iloc

import pandas as pd 

df=pd.read_csv('student_data.csv')
print(df,'\n')

df_index = df.set_index('StudentID')
print(df_index,'\n')
#It means that the original dataframe will be changed and the StudentId column will be set as index.
#Inplace=True means that the original dataframe will be modified and the changes will be applied to it directly. 
#If inplace=False (default), a new dataframe will be returned with the changes, and the original dataframe will remain unchanged.

print(df_index.iloc[0:3],'\n') #Ending index is excluded
print(df_index.iloc[:,0:5],'\n') #iloc is used to access rows and columns by their integer position.

df.rename(columns={'FullName':'Full Name','Algorithm Marks' :'Algo Marks'},inplace=True)
print(df,'\n')