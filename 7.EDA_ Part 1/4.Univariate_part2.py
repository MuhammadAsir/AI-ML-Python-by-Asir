import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#We will see numerical univariate analysis in this section.

df = pd.read_csv('titanic_data_updated.csv')
plt.title('Histogram of Age')
plt.xlabel('Ages')
plt.ylabel('frequency')
sns.histplot(data=df,x='Age',bins=20)
plt.show()

sns.kdeplot(df['Age'])
plt.title('KDE plot of Age')
plt.xlabel('Ages')
plt.ylabel('probabilty distribution')
plt.show()