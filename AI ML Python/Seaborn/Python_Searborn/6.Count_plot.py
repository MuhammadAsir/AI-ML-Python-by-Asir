import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

"""
Count plot is used to visualize the count of categorical data and it is used to visualize the distribution of the data.

"""

student= pd.read_csv('student_dataset_complete.csv') 
sns.countplot(data=student,x='subject',hue='gender')


#In barplot x axis is categorial and y axis is aggregate of data.example: category vs mean  

sns.barplot(data=student,x='gender',y='Marks',errorbar=None) #by default mean

sns.barplot(data=student,x='gender',y='Marks',errorbar=None,estimator=np.median) #median
sns.barplot(data=student,x='gender',y='Marks',errorbar=None,estimator=np.max) #max