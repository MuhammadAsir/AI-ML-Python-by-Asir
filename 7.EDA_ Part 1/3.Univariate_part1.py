import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

"""
Univariate analysis focuses on analyzing a single variable at a time.
It helps us understand the distribution, central tendency,
and variability of that variable."""
#We will see categorcal univariate analysis in this section.

df = pd.read_csv('titanic_data_updated.csv')

#sns.countplot(data=df,x='Survived')
#plt.show()

survived_count=df['Survived'].value_counts()
print(survived_count)

percentage=(survived_count/len(df))*100
print(percentage)
plt.title('Pie chart of survival rate')
survived_unique=df['Survived'].unique() 
#The unique() function is used to find the unique values in a column.
plt.pie(survived_count,labels=survived_unique,autopct='%1.1f%%')
plt.show()
