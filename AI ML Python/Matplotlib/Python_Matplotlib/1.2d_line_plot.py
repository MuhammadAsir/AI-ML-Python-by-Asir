"""Matplotlib is a plotting library for the Python programming language 
and its numerical mathematics extension NumPy. 
The use case of Matplotlib is to create 2D plots and graphs from data in arrays.
We need this library to visualize the data and to understand the data better.
"""

import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt


student_1 = [2 , 3 , 4, 1 , 5 , 7 , 3] 
student_2 = [ 1 , 4 , 3 , 5 ,7 ,2 ,1]
days = [1 ,2 , 3 ,4 ,5 ,6 ,7] 

plt.xlabel('Days')
plt.ylabel('Study Hours') 
plt.title('Trend of a student study time over a week')

plt.plot(days,student_1,label='Student 1')
plt.plot(days,student_2,label='Student 2') 
plt.legend()#It helps to identify different data series or categories represented in the plot.
plt.show()