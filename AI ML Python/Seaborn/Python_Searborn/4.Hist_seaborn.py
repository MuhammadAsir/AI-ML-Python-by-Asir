import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
#difference between axes level and figure level is that in axes level we can only plot one histogram at a time but in figure level we can plot multiple histograms in one figure.


student = pd.read_csv('student_dataset_complete.csv') 
sns.histplot(data=student,x='attendance_rate',hue='gender',element='step',bins=15)
#element='step' used for only outline of the histogram.
#plt.show()

#figure level
sns.displot(kind='hist',data=student,x='attendance_rate',col='gender')

plt.show()

"""why kind='hist' is not working in relplot()? 
because relplot() is used for relational plots like scatter and line plots, 
and it does not support histogram plots. 
To create a histogram, you should use sns.histplot() instead of sns.relplot()."""