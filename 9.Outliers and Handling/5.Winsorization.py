"""
Winsorization technique is a method of transforming data by limiting extreme values to reduce 
the influence of outliers.It is a robust method that can be used 
to handle outliers in a dataset without completely removing them.
It is better than Z-score and IQR method,
because it does not completely remove the outliers but limits their influence
by replacing them with the nearest non-outlier values.
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


df = pd.read_csv('marks_dataset.csv')
x = 12 #12% of the data will be considered as outliers and will be replaced with the nearest non-outlier values.
x = x/100
min_range = df['maths_marks'].quantile(x) 
max_range = df['maths_marks'].quantile(1-x) 
print(f"min range : {min_range} and max range: {max_range}")
df['maths_marks'] = df['maths_marks'].clip(min_range, max_range)
print(df['maths_marks'].describe())
