import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

"""
Regplot is used to visualize the linear relationship between two variables. 
It is used to visualize the scatter plot and the regression line. 
Mainly used in linear regression to visualize the relationship between the independent variable and the dependent variable.

"""

student= pd.read_csv('student_dataset_complete.csv') 

#axes level
sns.regplot(data=student,x ='study_hours' , y = 'test_score')


#figure level

sns.lmplot(data=student,x ='study_hours' , y = 'test_score',hue='gender') 
plt.show()