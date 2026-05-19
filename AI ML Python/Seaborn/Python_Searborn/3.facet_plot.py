import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px


student = pd.read_csv('student_dataset_complete.csv') 


sns.relplot(kind='scatter', data = student, x = 'study_hours' , y ='test_score',col='gender',row='hostel')
#So col will create column wise plot and row will create row wise plot
#in the dataset,hostel=0 means no one is living in hostel and hostel=1 means they are living in hostel
#plt.show()

sns.relplot(kind='scatter', data = student, x = 'study_hours' , y ='test_score',col='week',col_wrap=2)
#col_wrap will wrap the column into 2 columns
plt.show()