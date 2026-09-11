import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('titanic_data_updated.csv')

print(df.shape)

print(f"Total potential features: {df.shape[1]}")
#df.shape[1] means the number of columns in the dataframe, which represents the total potential features available for analysis.

print(f"Total sample data: {df.shape[0]}")
#df.shape[0] means the number of rows in the dataframe, which represents the total sample data or observations available for analysis.

print(df.sample(10))


#Missing values

print(df.isnull().sum())

#Duplicate values
print(df.duplicated().sum())
df.drop_duplicates(inplace=True)

"""For training a machine learning model, we can't give string or object data as input. 
We need to convert them into numerical data.

"""
print(df.info())