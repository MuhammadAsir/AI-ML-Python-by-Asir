import pandas as pd


df = pd.read_csv('student_data.csv')
df['Total Marks'] = df.iloc[::,2:5].sum(axis=1) 

df['EnrollmentDate']=pd.to_datetime(df['EnrollmentDate'])
print(df['EnrollmentDate'])

df['EnrollmentYear']=df['EnrollmentDate'].dt.year
df['EnrollmentDay']=df['EnrollmentDate'].dt.day
print(df[['EnrollmentYear','EnrollmentDay']])

"""df['FinishedDate']=pd.to_datetime(df['FinishedDate'])   

df['Total time taken to finish']= df['FinishedDate'] - df['EnrollmentDate']
print(df['Total time taken to finish'])
"""

