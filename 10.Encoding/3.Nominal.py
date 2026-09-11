
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OrdinalEncoder,OneHotEncoder

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

"""
Suppose we have a categorical variable "gender" with two categories:male and female
If we apply ordinal encoding to this variable, we might assign the following integer values:
male=0
female=1
However, this encoding implies that there is an order or hierarchy between the categories,
which may not be appropriate in this case.Female will get much priority then male.
That's why we use nominal encoding for such variables.
"""

gender_ohe=OneHotEncoder(sparse_output=False).set_output(transform='pandas')
#Sparse_output=False means that the output will be a dense array instead of a sparse matrix.
#set_output(transform='pandas') means that the output will be a pandas DataFrame instead of a NumPy array.

gender_ohe.fit(x_train[['Sex']])
encoded_df=gender_ohe.transform(x_train[['Sex']])
x_train=pd.concat([x_train,encoded_df], axis=1)
encoded_df=gender_ohe.transform(x_test[['Sex']])
x_test=pd.concat([x_test,encoded_df], axis=1)
print(x_train)