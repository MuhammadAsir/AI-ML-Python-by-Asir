
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OrdinalEncoder,OneHotEncoder
from sklearn.preprocessing import LabelEncoder
#label encoding is a technique used to convert categorical variables into numerical format. It assigns a unique integer to each category in the variable. 

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


le=LabelEncoder()

le.fit(y_train)

y_train_encoded=le.transform(y_train)
y_test_encoded=le.transform(y_test)

y_train = pd.Series(y_train_encoded,index = y_train.index , name = y_train.name)
#The line of code creates a new pandas Series called y_train, which contains the encoded values of the original y_train variable. The index and name of the new Series are set to be the same as the original y_train variable. This allows us to maintain the same structure and labeling for the encoded target variable while replacing the original categorical values with their corresponding integer labels.
y_test = pd.Series(y_test_encoded,index = y_test.index , name = y_test.name)
print(y_train)