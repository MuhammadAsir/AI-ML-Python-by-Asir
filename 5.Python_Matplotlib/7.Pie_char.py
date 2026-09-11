import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt

df = pd.read_csv('student_data.csv')

status=df.groupby('CompletionStatus').size()
plt.pie(status,labels=status.index,autopct='%1.1f%%',colors=['green','yellow','red'],shadow=True,explode=(0.1,0.1,0.1))
#autopct='%1.1f%%' is used to display the percentage of each slice on the pie chart. It formats the percentage to one decimal place and adds a percent sign.
#expload is used to separate the slices of the pie chart. In this case, we are separating all three slices by 0.1 units.

plt.title('Pie Chart of Course completion')
plt.show() 
