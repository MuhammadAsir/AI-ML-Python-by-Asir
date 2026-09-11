"""
Robust Scaler is another feature scaling technique that is specifically designed 
to handle outliers better than Min-Max Scaling and Standardization.
Formula:
X_scaled = (X - median) / IQR

Why Does It Use Median and IQR?
Mean and standard deviation are affected by extreme values.
Median and IQR are much more resistant to outliers.

Use it when:
Dataset contains many outliers
Outliers are genuine data points (you don't want to remove them)
Median and IQR represent the data better than mean

Examples:House prices,Income data,Sales data

"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import RobustScaler


df = pd.read_csv('marks_dataset.csv')
print(df['maths_marks'].describe())
rs = RobustScaler()

rs.fit(df[['maths_marks']])

df['maths_marks']= rs.transform(df[['maths_marks']]).ravel()
sns.kdeplot(data =df , x = 'maths_marks')
plt.show()

print(df['maths_marks'].describe()) 
#So we used robust scaler in maths marks because it has many outliers and we can see that after applying robust scaler the distribution is more normal and the outliers are handled better than min-max scaling and standardization.