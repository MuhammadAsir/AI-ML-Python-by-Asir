import pandas as pd 

df=pd.read_csv('student_data.csv')
print(df,'\n')

#df.sort_values('Data Structure Marks') created a copy. so we have to store it in a variable.
CPY=df.sort_values('Data Structure Marks',ascending=False)
print(CPY,'\n')



copy=df.sort_values(['Data Structure Marks','Python Marks'],ascending=[False,True])
print(copy,'\n')    
#it means ascending order for python marks and descending order for data structure marks.