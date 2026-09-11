import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

"""
KDE is a non-parametric way to estimate the probability density function of a random variable.
it is used for continuous data and it is a smoothed version of the histogram. 
it is used to visualize the distribution of the data.
Difference between histogram and KDE plot is that histogram is a discrete representation of the data 
while KDE plot is a continuous representation of the data.

"""

student= pd.read_csv('student_dataset_complete.csv') 
sns.kdeplot(data = student , x ='attendance_rate',hue='gender',fill=True)
#fill=True is used to fill the area under the curve with color. 

sns.displot(kind='kde',data=student,x='attendance_rate',col='gender')

plt.show()