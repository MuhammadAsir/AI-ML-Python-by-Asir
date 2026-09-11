"""
MinMax Scaler is a technique used to scale features to a specific range, 
typically between 0 and 1. It works by transforming the data using the following formula:
X_scaled = (X - X_min) / (X_max - X_min)

Use Min-Max Scaling When
-Data has no significant outliers
-You need values between 0 and 1
-Neural Networks often benefit from this
-Image processing (pixel values 0–255 → 0–1)

Example:
Algorithm: Neural Networks,KNN,K-Means


"""


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import MinMaxScaler

df = pd.read_csv('titanic_data_updated.csv')

df.drop(['PassengerId','Name','Ticket'], axis=1, inplace=True)
  

x=df.drop('Survived', axis=1) 
y=df['Survived'] 


x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2, random_state=42)


age_imputer=SimpleImputer(missing_values=np.nan ,strategy='mean') 
age_imputer.fit(x_train[['Age']]) 
x_train['Age']=age_imputer.transform(x_train[['Age']]).ravel() 

x_test['Age']=age_imputer.transform(x_test[['Age']]).ravel()


embarked_imputer=SimpleImputer(missing_values=np.nan ,strategy='most_frequent')
embarked_imputer.fit(x_train[['Embarked']])
x_train['Embarked']=embarked_imputer.transform(x_train[['Embarked']]).ravel()   
x_test['Embarked']=embarked_imputer.transform(x_test[['Embarked']]).ravel()

cabin_imputer=SimpleImputer(missing_values=np.nan ,strategy='constant', fill_value='Missing',add_indicator=True)

cabin_imputer.fit(x_train[['Cabin']])

x_train[['Cabin','Cabin_Missing']]=cabin_imputer.transform(x_train[['Cabin']])
x_test[['Cabin','Cabin_Missing']]=cabin_imputer.transform(x_test[['Cabin']])


mm=MinMaxScaler()#Creating an instance of the MinMaxScaler class to perform min-max scaling.

mm.fit(x_train[['Fare']])    
x_train['Fare'] = mm.transform(x_train[['Fare']]).ravel()
x_test['Fare'] = mm.transform(x_test[['Fare']]).ravel()

print(x_train['Fare'].describe())   

