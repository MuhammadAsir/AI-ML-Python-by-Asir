import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#We will see numerical univariate analysis in this section part 2.

df = pd.read_csv('titanic_data_updated.csv')
sns.histplot(df['Fare'],bins=50)

plt.title('Histogram of Fare')
plt.xlabel('Fare')
plt.ylabel('frequency')
plt.show()


sns.kdeplot(df['Fare'])
plt.title('KDE plot of Fare')
plt.xlabel('Fare')
plt.ylabel('probabilty distribution')
plt.show()


sns.boxplot(df['Fare'])
plt.show() 
#By using boxplot we can see Fare has outliers. 