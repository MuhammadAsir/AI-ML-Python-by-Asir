""" Searborn is a Python data visualization library based on matplotlib. 
It provides a high-level interface for drawing attractive and informative statistical graphics. 
It is used in data analysis and machine learning to visualize data distributions, 
relationships, and trends.
Plotly is a graphing library that makes interactive, publication-quality graphs online."""
#Install seaborn using python -m pip install seaborn, then python -m pip install plotly


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

student = pd.read_csv('sns_data.csv') 

sns.lineplot(data=student,x='week',y='attendance_rate',errorbar=None,hue='gender')
#hue is a parameter in seaborn that allows you to group data by a categorical variable and assign different colors to each group in the plot.
plt.grid()
plt.show()

"""
sns.replot(kind='line',data=student,x='week',y='attendance_rate',errorbar=None,hue='gender')

So replot will create a new figure and plot the data, 
while lineplot will plot the data on the current figure.
kind is a parameter in seaborn that specifies the type of plot to create.
"""