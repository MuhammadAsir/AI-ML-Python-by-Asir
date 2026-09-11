
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

#Z score is better in normal distribution and I have checked that age column is normally distributed by plotting histogram and boxplot.
mean_of_age = x_train['Age'].mean()
std_of_age = x_train['Age'].std()
x_train['zscore_Age'] = (x_train['Age']-mean_of_age)/std_of_age
outliers_age=x_train[abs(x_train['zscore_Age'])>3]


#IQR is better in skewed distribution and I have checked that fare column is skewed by plotting histogram and boxplot.
fare_Q1 = x_train['Fare'].quantile(0.25)
fare_Q3 = x_train['Fare'].quantile(0.75)

fare_IQR = fare_Q3 - fare_Q1
fare_minimum = max(0,fare_Q1 - 1.5 * fare_IQR) 
fare_maximum = fare_Q3 + 1.5 * fare_IQR

x_train['Fare']=x_train['Fare'].clip(fare_minimum,fare_maximum)
"""
clip function is used to replace the outliers with the minimum and maximum values calculated using IQR method.
If the value is less than minimum it will be replaced with minimum 
and if the value is greater than maximum it will be replaced with maximum.
"""
print(x_train['Fare'].describe()) #after clipping the outliers in fare column