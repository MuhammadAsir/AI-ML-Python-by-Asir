import pandas as pd

df = pd.read_csv('student_data.csv')
df['Total Marks'] = df.iloc[::,2:5].sum(axis=1) 



instructor_group = df.groupby('Instructor')
print(instructor_group)

for instructor, df_ins in instructor_group:
     print(instructor)
     print(df_ins)
    
"""instructor_group.min() ,it will show the minimum value of each column for each instructor
instructor_group.describe(), it will show the statistical summary of each column for each instructor


mean_marks = instructor_group['Total Marks'].mean(),
it will show the average marks of each instructor

df['Total Marks']= df['Total Marks'].fillna(df['Instructor'].map(mean_marks)), 
it will fill the missing values in the 'Total Marks' column with the average marks of the respective instructor
"""

