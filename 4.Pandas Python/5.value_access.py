import pandas as pd 

df=pd.read_csv('student_data.csv')
print(df)

#accessing a column
print(df['FullName'],type(df['FullName']),'\n')

# df.loc[ind start:ind end,col_start,col_end]
print(df.loc[0],'\n') #showing the first row of the dataframe

# multiple row ( normal list ) 
print(df.loc[[1,2,3]],'\n')

# multiple row (range)
print(df.loc[5:9],'\n') #Ending index is included

# single column 
print(df.loc[:,'Python Marks'],'\n')

#multiple column 


print(df.loc[:,['Python Marks','Algorithm Marks']])
print(type(df.loc[:,['Python Marks','Algorithm Marks']]),'\n')

print(df.loc[0:5,['FullName','Python Marks']],'\n')

