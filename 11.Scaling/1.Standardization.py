"""
Standardization is a technique used to transform data to have a mean of zero 
and a standard deviation of one. 

Use Standardization When
-Data contains outliers
-Data is approximately normally distributed
-Features have different scales
-You are unsure which scaler to use

Example:
Algorithm:-Linear Regression,Logistic Regression,SVM,PCA,Gradient Descent-based algorithms

"""


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler

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


ss=StandardScaler()#Creating an instance of the StandardScaler class to perform standardization.

ss.fit(x_train[['Age']])
x_train['Age'] = ss.transform(x_train[['Age']]).ravel()
x_test['Age'] = ss.transform(x_test[['Age']]).ravel()
#So we used Z-score standardization to transform the 'Age' feature in both the training and testing datasets.

print(round(x_train['Age'].mean(),5)) 
print(round(x_train['Age'].std(),5)) 
print(x_train.head())
sns.kdeplot(data = x_train , x ='Age')
plt.show()
# we can see that the distribution of the 'Age' feature has been standardized, with a mean of approximately 0 and a standard deviation of 1.