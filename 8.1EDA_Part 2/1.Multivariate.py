import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

"""
Multivaiate Analysis is the process of analyzing data that contains more than one variable. 
It is used to understand the relationships between variables and to identify patterns in the data.
 Multivariate analysis can be used for a variety of purposes, including:
1. Identifying correlations between variables
2. Building predictive models
3. Reducing the dimensionality of the data
etc.
"""

# Multivariate Analysis- 1 ( Countplot with Hue )
df = pd.read_csv('titanic_data_updated.csv')
  
sns.countplot(x=df['Sex'],hue=df['Survived'])
#plt.show()

gender_group=df.groupby('Sex')['Survived'].value_counts() 
#It Splits the data of Male and Female and counts the number of Survived and Not Survived in each group.
print(gender_group)

"""
sns.countplot(x=df['Pclass'],hue=df['Survived'])

pclass_split = df.groupby('Pclass')['Survived'].value_counts(normalize=True)

print(pclass_split)
"""