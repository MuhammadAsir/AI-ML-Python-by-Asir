import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

#Pairplot is used to visualize the pairwise relationships between the variables in a dataset.

student= pd.read_csv('student_dataset_complete.csv') 

student_marks = student[['Marks','study_hours','attendance_rate','gender']]

sns.pairplot(data=student_marks,hue='gender')

"""
Based on the dataset it will show the relationship between marks and study hours, 
marks and attendance rate, study hours and attendance rate. 
It will also show the distribution of each variable on the diagonal.
It will show scatter,kde and histogram plots for the pairwise relationships between the variables.
"""

sns.pairplot(data=student_marks, kind='hist')
