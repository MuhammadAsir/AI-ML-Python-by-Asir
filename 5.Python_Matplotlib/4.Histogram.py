import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt

students = pd.read_csv('student_IQdata.csv')
plt.xlabel('IQ Score') 
plt.ylabel('Frequency of Students') 
plt.hist(students['IQ_Score'],color='Red',edgecolor='black',bins=10)
#bins is used to specify the number of bins in the histogram.
plt.show()

"""
Histogram is a graphical representation of the distribution of a dataset. 
It is used to show the frequency of data points within certain ranges (bins). 
The x-axis represents the range of values, 
while the y-axis represents the frequency of data points within each bin.
"""