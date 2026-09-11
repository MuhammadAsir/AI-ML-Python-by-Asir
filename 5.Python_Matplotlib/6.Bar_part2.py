import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt

df = pd.read_csv('student_data.csv')

status = df.groupby('CompletionStatus').size() 
#We have written size() instead of count() because we want to count the number of rows in each group, and size() does exactly that. On the other hand, count() would count the number of non-null values in each group, which may not give us the correct count if there are any missing values in the 'CompletionStatus' column.

plt.bar(status.index,status.values,color=['green','orange','red'],edgecolor='black')

plt.xlabel('Completion Status') 
plt.ylabel('Count') 
plt.title('Bar Chart of Course completion')
plt.show() 