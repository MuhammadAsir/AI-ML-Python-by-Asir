import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.impute import SimpleImputer
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OrdinalEncoder,OneHotEncoder,LabelEncoder,StandardScaler,MinMaxScaler
"""
Column Transformer is a Scikit-Learn utility that allows us to apply
different preprocessing techniques to different columns of a dataset
within a single transformation pipeline.

Age, Salary → Scaling, missing values imputation
Gender, City → Encoding

Instead of preprocessing each column separately,
we can do everything in one pipeline using ColumnTransformer.

"""

df = pd.read_csv('titanic_data_updated.csv')
df.drop(['PassengerId','Name','Ticket'],axis=1,inplace=True)

x = df.drop(['Survived'],axis=1)
y = df['Survived']

x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.2,random_state=42)

#variable=ColumnTransformer(name,transformer,columns)

#Imputation of data
imputer_transformer=ColumnTransformer(
    transformers=[
        ('age',SimpleImputer(missing_values=np.nan,strategy='mean'),['Age']),
        ('embarked',SimpleImputer(missing_values=np.nan,strategy='most_frequent'),['Embarked']),
        ('cabin',SimpleImputer(missing_values=np.nan,strategy='constant',fill_value='missing',add_indicator=True),['Cabin'])
    ],
    remainder='passthrough', #This means that any columns not specified in the transformers list will be left unchanged and passed through to the output without any transformation.
    verbose_feature_names_out=False #This means that the output feature names will be the same as the input feature names, without any additional prefixes or suffixes.
)

imputer_transformer.set_output(transform='pandas')
#This means that the output of the transformation will be a pandas DataFrame instead of a NumPy array. 

imputer_transformer.fit(x_train)#This step calculates the necessary statistics (like mean for 'Age' and 'Fare', and most frequent value for 'Embarked') from the training data to perform the imputation.
x_train = imputer_transformer.transform(x_train)
x_test = imputer_transformer.transform(x_test)

#outlier handling of age
mean_of_age = x_train['Age'].mean()
std_of_age = x_train['Age'].std()
x_train['zscore_Age'] = (x_train['Age']-mean_of_age)/std_of_age

x_train = x_train[abs(x_train['zscore_Age']) <=3]#This line filters the training data to include only those rows where the absolute value of the z-score for the 'Age' column is less than or equal to 3. In other words, it removes any rows where the 'Age' value is considered an outlier based on the z-score threshold of 3.
x_train.drop(['zscore_Age'],axis=1 , inplace=True)

#outlier handling of fare
fare_Q1 = x_train['Fare'].quantile(0.25)
fare_Q3 = x_train['Fare'].quantile(0.75)
fare_IQR = fare_Q3 - fare_Q1
fare_minimum = max(0,fare_Q1 - 1.5 * fare_IQR)
fare_maximum = fare_Q3 + 1.5 * fare_IQR

x_train['Fare']= x_train['Fare'].clip(fare_minimum , fare_maximum)
#This means that any values in the 'Fare' column that are less than the calculated minimum will be set to the minimum value, and any values greater than the calculated maximum will be set to the maximum value. This is a common technique for handling outliers in a dataset, as it helps to reduce the influence of extreme values while still retaining all data points.

#encoding and scaling
encoder_scaler = ColumnTransformer(
    transformers=[
        ('pclass',OrdinalEncoder(categories=[['third','second','first']]),['Pclass']),
        ('embarked_sex',OneHotEncoder(sparse_output=False,drop='first'),['Embarked','Sex','Cabin_Deck']),
        ('age_scaler',StandardScaler(),['Age']),
        ('fare_scaler',MinMaxScaler(),['Fare','FamilySize'])
    ],
    remainder='passthrough',
    verbose_feature_names_out = False
)
encoder_scaler.set_output(transform='pandas')

encoder_scaler.fit(x_train)

x_train = encoder_scaler.transform(x_train)
x_test = encoder_scaler.transform(x_test)

x_train.drop(['Cabin','SibSp','Parch'],axis=1,inplace=True)
x_test.drop(['Cabin','SibSp','Parch'],axis=1,inplace=True)

"""
So we used column transformer to do all the preprocessing steps in one pipeline and 
it is more efficient than doing each step separately. 
It also helps to avoid data leakage 
and ensures that the same transformations are applied to both training and testing data."""