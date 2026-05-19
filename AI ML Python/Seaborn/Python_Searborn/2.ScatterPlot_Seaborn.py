import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

student = pd.read_csv('sns_data.csv') 

#style is a argument that allows us to differentiate data points based on a categorical variable by using different marker styles. 
#size is a argument that allows us to differentiate data points based on a numerical variable by using different marker sizes.

# We will use replot for better visualization and to add grid to the plot
sns.relplot(kind='scatter', data = student , x = 'study_hours' , y ='test_score',hue='gender',style='subject',size='Tshirt_size') 
plt.grid()
plt.show()

tips_data=sns.load_dataset("tips")
sns.relplot(kind='scatter',data=tips_data,x='total_bill',y='tip',hue='day',style='time',size='size')
plt.grid()
plt.show()


