import pandas as pd
import numpy as np
df=pd.read_csv('student_data.csv')
print(df,'\n')

#add new column

df['Country']='Bangladesh'
print(df,'\n')

df['Total Marks']=df['Data Structure Marks']+df['Python Marks']+df['Algorithm Marks']
print(df,'\n')

df['A+ in DS']=np.where(df['Data Structure Marks']>=80,'Yes','No')
print(df,'\n')


df['First Name']=df['FullName'].str.split(' ').str[0]
print(df,'\n')

df1=pd.read_csv('student_data.csv')
print(df1,'\n')

#df is modified but df1 is not modified because we have created a new dataframe df1 and we have not done any modification in df1. So, df1 is same as original data.
df.to_csv('new_student_data.csv')
#it means we have created a new csv file with name new_student_data.csv and we have saved the modified dataframe df in that new csv file. So, now we have two csv files one is original student_data.csv and another is new_student_data.csv which contains the modified data.