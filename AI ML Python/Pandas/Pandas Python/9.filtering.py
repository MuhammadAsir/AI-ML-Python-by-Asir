import pandas as pd 

df=pd.read_csv('student_data.csv')
print(df,'\n')


not_started=df.loc[df['CompletionStatus']=='Not Started']
print(not_started,'\n') 

# completed and ds marks is greater or equal 90 
completed_ds90 = df.loc[(df['CompletionStatus']=='Completed') & (df['Data Structure Marks']>=90)]
print(completed_ds90,'\n')