
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.impute import SimpleImputer


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


age_q1 = x_train['Age'].quantile(0.25)
age_q3 = x_train['Age'].quantile(0.75)

age_iqr = age_q3 - age_q1

min_age = age_q1 - 1.5*age_iqr #It means that any value below this will be considered as an outlier
max_age= age_q3 + 1.5*age_iqr #It means that any value above this will be considered as an outlier
print(f"Age column: min value for outliers: {min_age}")
print(f"Age column: max value for outliers: {max_age}")

age_outlier_iqr=x_train[(x_train['Age']<min_age)| (x_train['Age']>max_age)]
print(len(age_outlier_iqr)) #total 54 outliers in age column


fare_Q1 = x_train['Fare'].quantile(0.25)
fare_Q3 = x_train['Fare'].quantile(0.75)

fare_IQR = fare_Q3 - fare_Q1

fare_minimum = max(0,fare_Q1 - 1.5 * fare_IQR) #Since fare cannot be negative, we take the maximum of 0 and the calculated minimum to ensure that we do not consider negative values as outliers.
fare_maximum = fare_Q3 + 1.5 * fare_IQR
print(fare_minimum , fare_maximum)

fare_outlier_IQR = x_train[(x_train['Fare']<fare_minimum) | (x_train['Fare']>fare_maximum)]

print(len(fare_outlier_IQR))# total 96 outliers in fare column