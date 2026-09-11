import pandas as pd


df = pd.read_csv('student_data.csv')
print(df,'\n')

  

print(df.dropna(),'\n')#it will drop all the rows which have null values

df.dropna(how='all', inplace=True) #it will drop only those rows which have all values as null

df.dropna(subset=['Python Marks'])#it will drop only those rows which have null values in the 'Python Marks' column

df.fillna(0) #it will replace all the null values with 0. You can replace it with any value you want, like mean, median, etc.

df['FullName'].fillna('Unknown', inplace=True) #it will replace all the null values in the 'FullName' column with 'Unknown'

df['Python Marks'].fillna(df['Python Marks'].mean(), inplace=True) #it will replace all the null values in the 'Python Marks' column with the mean of that column