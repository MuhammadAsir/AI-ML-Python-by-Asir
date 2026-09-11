
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

print(x_train['Cabin'].value_counts())
print(x_train['Cabin'].dtype)

x_train['Cabin_Deck']=x_train['Cabin'].astype(str).str[0]
#It extracts the first character of the 'Cabin' column and assigns it to a new column called 'Cabin_Deck'.

x_test['Cabin_Deck']=x_test['Cabin'].astype(str).str[0]

print(x_train['Cabin_Deck'].value_counts())


encode_deck=OneHotEncoder(sparse_output=False,drop='first').set_output(transform='pandas')
#drop='first' means that the first category will be dropped to avoid multicollinearity.Because if we have n categories, we only need n-1 dummy variables to represent them.

encode_deck.fit(x_train[['Cabin_Deck']])

encoded_df=encode_deck.transform(x_train[['Cabin_Deck']])
x_train=pd.concat([x_train,encoded_df], axis=1)
encoded_df=encode_deck.transform(x_test[['Cabin_Deck']])
x_test=pd.concat([x_test,encoded_df], axis=1)

x_train.drop('Cabin_Deck',axis=1, inplace=True)
x_test.drop('Cabin_Deck',axis=1, inplace=True)

print(x_train.head())