import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Multi Variate Analysis -3 ( Barplot for Cat-Num)
#With Barplot we can analyze the relationship between a categorical variable and a numerical variable.
#Barplot y axis is measure of central tendency (mean) and x axis is categorical variable.

df = pd.read_csv('titanic_data_updated.csv')


sns.barplot(x=df['Pclass'],y=df['Fare'],errorbar=None)
plt.show()

sns.barplot(x=df['Survived'],y=df['Age'],hue=df['Sex'],errorbar=None)
plt.show()