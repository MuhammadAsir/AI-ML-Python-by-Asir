import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt

df = pd.read_csv('enrollment_data.csv') 
plt.xlabel('Year')
plt.ylabel('Enrollment')
plt.title('Enrollment Trend Over Years')
plt.plot(df['Year'], df['Programming'],label='Programming',marker='o',linewidth=2)
plt.plot(df['Year'],df['Digital Marketing'],label='Digital Marketing',marker='o',linewidth=2)
plt.legend()#it works as a key to identify the line in the graph
plt.grid()
plt.show()