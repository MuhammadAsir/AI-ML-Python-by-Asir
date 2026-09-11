"""
Feature Engineering is a crucial step in the data science process, 
where raw data is transformed into meaningful features that can be used for machine learning models.
This process involves selecting, modifying,
or creating new features from the existing data to improve the performance of the model.

Scikit-learn is a powerful library in Python that provides various tools for feature engineering

"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.impute import SimpleImputer

#from sklearn.impute import SimpleImputer is used to handle missing values in the dataset.

df = pd.read_csv('titanic_data_updated.csv')

df.drop(['PassengerId','Name','Ticket'], axis=1, inplace=True)
  

x=df.drop('Survived', axis=1) #x is the feature set, which includes all the columns except 'Survived'.  
y=df['Survived'] #y is the target variable, which is the 'Survived' column that we want to predict.


x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2, random_state=42)
#random_state=42 means that the data will be split in the same way every time you run the code, ensuring reproducibility.

x_train.isnull().sum()
x_test.isnull().sum()


#Mean imputation is a technique used to handle missing values in a dataset by replacing them with the mean value of the respective feature.
age_mean=x_train['Age'].mean()
x_train['Age_Mean_Imputor']=x_train['Age'].fillna(age_mean)
x_test['Age_Mean_Imputor']=x_test['Age'].fillna(age_mean)

# We can also use Median imputation, which replaces missing values with the median value of the respective feature.
sns.kdeplot(data=x_train,x='Age_Mean_Imputor')
plt.show()

#For Numerical values, we can use mean or median imputation to fill in missing values.
#For categorical values, we can use mode imputation
#If data is skewed, median imputation is often preferred over mean imputation
#If data is normally distributed, mean imputation can be a good choice 

"""We will learn simple imputation technique to handle missing values in the dataset.
from sklearn.impute import SimpleImputer is used to handle missing values in the dataset.

fillna vs SimpleImputer:
fillna is a method provided by pandas that allows you to fill missing values in a DataFrame or Series with a specified value or method (e.g., mean, median, mode). It is a simple and straightforward way to handle missing data.
SimpleImputer, on the other hand, is a class from the sklearn library that provides more advanced imputation techniques. It allows you to specify the strategy for imputation (e.g., mean, median, most_frequent) and can be used in a pipeline with other preprocessing steps. SimpleImputer is particularly useful when you want to apply the same imputation strategy to both training and test data without data leakage.

"""

#Numerical Missing Values Imputation using Simple Imputer
age_imputer=SimpleImputer(missing_values=np.nan ,strategy='mean') 
age_imputer.fit(x_train[['Age']]) #fit the imputer on the training data to calculate the mean value of the 'Age' column.
#Why double brackets? Because the fit method expects a 2D array, and x_train[['Age']] returns a DataFrame (which is 2D), while x_train['Age'] would return a Series (which is 1D).

x_train['Age']=age_imputer.transform(x_train[['Age']]).ravel() #transform the 'Age' column in the training data by replacing missing values with the mean value calculated during fitting.
#ravel() is used to convert the output of the transform method, which is a 2D array, back into a 1D array that can be assigned to the 'Age' column in the DataFrame.It is used  for better Machine Learning model performance, as many models expect the input features to be in a 1D format.

#We are not fitting x_test[['Age']], because we want to use the same mean value calculated from the training data.We should not fit the imputer on the test data, as it would lead to data leakage and give us an unrealistic performance estimate.
x_test['Age']=age_imputer.transform(x_test[['Age']]).ravel()

x_train.drop('Age_Mean_Imputor', axis=1, inplace=True)
x_test.drop('Age_Mean_Imputor', axis=1, inplace=True)



#Categorical Value Imputation with Mode Value
embarked_imputer=SimpleImputer(missing_values=np.nan ,strategy='most_frequent')
embarked_imputer.fit(x_train[['Embarked']])
x_train['Embarked']=embarked_imputer.transform(x_train[['Embarked']]).ravel()   
x_test['Embarked']=embarked_imputer.transform(x_test[['Embarked']]).ravel()



#Categorical Value Imputation with Missing string and Indicator
cabin_imputer=SimpleImputer(missing_values=np.nan ,strategy='constant', fill_value='Missing',add_indicator=True)
#It means that the imputer will replace missing values with the string 'Missing' and also add an indicator column to indicate which values were imputed.
cabin_imputer.fit(x_train[['Cabin']])

x_train[['Cabin','Cabin_Missing']]=cabin_imputer.transform(x_train[['Cabin']])
x_test[['Cabin','Cabin_Missing']]=cabin_imputer.transform(x_test[['Cabin']])
print(x_train.isnull().sum())  #So there is no missing value in the dataset now.
#We can't use ravel() here because we are transforming two columns at once, and the output will be a 2D array that cannot be flattened into a 1D array. Instead, we assign the transformed values back to the original columns in the DataFrame.