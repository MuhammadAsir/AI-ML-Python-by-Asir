import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt

"""
Bar chart is a graphical representation of data using bars of different heights. 
It is used to compare different categories or groups of data. 
The height of each bar represents the value of the data for that category.
Difference between histogram and bar chart is that histogram is used 
to show the distribution of a dataset, 
while bar chart is used to compare different categories or groups of data.
"""

data = {
    'Student': [ 'B', 'C', 'D', 'E', 'F', 'G', 'H'],
    'Gender': [ 'Male', 'Female', 'Male', 'Female', 'Male', 'Female', 'Male'],
    'StudyHours': [ 2, 5, 3, 7, 4, 8, 1],
    'Attendance': [ 60, 88, 70, 95, 80, 98, 55],
    'Grade': [ 'Fail', 'Pass', 'Fail', 'Pass', 'Pass', 'Pass', 'Fail']
}

df=pd.DataFrame(data)
print(df)

gender_group=df.groupby('Gender').size()

plt.bar(gender_group.index,gender_group.values,color=['blue','pink'],edgecolor='black') 
#Index is used to specify the categories (x-axis) and values is used to specify the height of the bars (y-axis).
plt.show()



