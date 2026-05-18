"""
Pandas is a library used for data manipulation and analysis.
It provides powerful data structures like Series and DataFrame, 
which allow for easy manipulation of data.
Pandas is widely used in data science and machine learning for tasks such as data cleaning,
NumPy → focuses on speed and mathematical computation (arrays without labels)
Pandas → focuses on data analysis with rows, columns, and labels"""

import pandas as pd 

df=pd.read_csv('student_data.csv') 
"""We read a CSV file (student_data.csv) using read_csv and store it in a DataFrame df. 
A DataFrame is a 2D table that can hold different types of data. After loading, 
we can analyze and modify the data, and print df to view it.."""

print(type(df),'\n',df)

#print Student id

student_id = df['StudentID'] 

print(type(student_id),'\n',student_id)
#it has type of series,which means it is a one-dimensional array with labels (the column name 'StudentID').
