import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt

#Scatter Plots are used to show the relationship between two variables.

students = pd.read_csv('student_IQdata.csv')
plt.xlabel('Study Hours') 
plt.ylabel('IQ Score') 
plt.title('Relation between Study Hours and IQ Score') 
plt.scatter(students['Study_Hour'], students['IQ_Score'], color='blue')
plt.grid()
plt.show()

"""
 Usage of scatter plot is to find the correlation between two variables.
 If the points are close to each other, then there is a strong correlation. 
 If the points are far from each other, then there is a weak correlation. 
 If the points are randomly scattered, then there is no correlation.
 We used it in Machine Learning to find the relationship between two variables."""