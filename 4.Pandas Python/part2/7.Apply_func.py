import pandas as pd


df = pd.read_csv('student_data.csv')
df['Total Marks'] = df.iloc[::,2:5].sum(axis=1) 

mn=df['Total Marks'].min()
mx=df['Total Marks'].max()

# Now we will scale the total marks between 0 and 1 using the formula (x-min)/(max-min)

df['Scaled Total Marks'] = df['Total Marks'].apply(lambda x: (x-mn)/(mx-mn))
print(df) 


def grading_system(marks):
    if marks>=260:
        return 'A+'
    elif marks>=250:
        return 'A'
    else:
        return 'B+'
    
df['Grade']=df['Total Marks'].apply(grading_system)
print(df)