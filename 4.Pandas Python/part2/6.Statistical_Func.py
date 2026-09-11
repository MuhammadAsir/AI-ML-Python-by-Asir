import pandas as pd


df = pd.read_csv('student_data.csv')

print(df['Data Structure Marks'].max())
print(df['Data Structure Marks'].min())
#we can also get mean,median, sum, count, std deviation, mode,variance etc

print(df['Data Structure Marks'].mode())

print(df[['Data Structure Marks','Python Marks']].corr())#correlation between two columns
print('\n')
print(df[['Data Structure Marks','Python Marks']].sum(axis=0))
print('\n')
#axis=0 means we want to sum the columns, if we want to sum the rows then we can use axis=1
print(df[['Data Structure Marks','Python Marks']].sum(axis=1))

#Alternative of df['Total Marks']=df['Data Structure Marks']+df['Python Marks'] is
df['Total Marks'] = df.iloc[::,2:5].sum(axis=1) 
print(df)