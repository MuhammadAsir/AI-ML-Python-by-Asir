import pandas as pd 

df=pd.read_csv('student_data.csv')
print(df,'\n')

#row deletion

df.drop(0,inplace=True) #drop the row with index 0  
print(df,'\n')

#column deletion

df.drop('Instructor',axis=1,inplace=True) #drop the column with name 'Instructor'
#axis=1 means that we want to drop a column. If axis=0, it means we want to drop a row.
print(df,'\n')


df.loc[1,'Python Marks']=90 
#it means that we want to change the value of the cell in the row with index 1 and the column 'Python Marks' to 90.
print(df,'\n')

df.loc[3:5,'Python Marks']+=2
print(df,'\n')
#it means 3 to 5 column python marks will be increased by 2


for i,series in df.iterrows():
    print(f"{i}:{series}",'\n')

print('\n')

for i in df.itertuples():
    print(i,'\n')