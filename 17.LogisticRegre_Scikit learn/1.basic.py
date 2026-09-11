import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OrdinalEncoder,OneHotEncoder,LabelEncoder,StandardScaler,MinMaxScaler

from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.metrics import accuracy_score,precision_score,recall_score
from sklearn.linear_model import LogisticRegression



df = pd.read_csv("titanic_data_updated.csv")

df['Family_Size'] = df['SibSp'] + df['Parch'] + 1
#It means we are creating a new column called Family_Size by adding the values of the SibSp and Parch columns and adding 1 to account for the passenger themselves. This gives us the total number of family members on board for each passenger.

df['Cabin'] = df['Cabin'].fillna("Missing")#It means we are filling the missing values in the Cabin column with the string "Missing". This is done to handle the missing data and ensure that all passengers have a value for the Cabin column.

df['Deck'] = df['Cabin'].astype(str).str[0]
#it means we are taking the first character of the Cabin column to create a new column called Deck. This is because the first character of the Cabin value represents the deck level on the ship. For example, if the Cabin value is "C123", then the Deck value will be "C". If the Cabin value is missing, we fill it with "Missing" and the Deck value will also be "M".

df['Deck'].value_counts()

x = df.drop('Survived', axis=1)
y = df['Survived']

# Split data: 80% for training the model and 20% for testing its accuracy
# 'stratify=y' ensures both sets have a similar percentage of survivors
X_train, X_test, Y_train, Y_test = train_test_split(x, y, test_size=0.2, random_state=42, stratify=y)

# numerical
p1 = Pipeline(
    steps=[
        ('imputer',SimpleImputer(strategy='mean')),
        ('scaler',StandardScaler())
    ]
)

p2 = Pipeline(
    steps=[
        ('imputer',SimpleImputer(strategy='median')),
        ('scaler',MinMaxScaler())
    ]
)

#  categorical columns

p3 = Pipeline(
    steps=[
        ('imputer',SimpleImputer(strategy='most_frequent')),
        ('encoder',OneHotEncoder(sparse_output=False,drop='first',handle_unknown='ignore'))
    ]
)

# categories goes one after another via stricly following the order of the input
categories = [['third','second','first']]
p4 = Pipeline(
    steps=[
        ('imputer',SimpleImputer(strategy='most_frequent')),
        ('encoder',OrdinalEncoder(categories=categories)),
        ('scaler',MinMaxScaler())
    ]
)

preprocessor = ColumnTransformer(
    transformers=[
        ('pipeline_1',p1,['Age']),
        ('pipeline_2',p2,['Fare','Family_Size']),
        ('pipeline_3',p3,['Embarked','Sex','Deck']),
        ('pipeline_4',p4,['Pclass'])
    ],
    remainder='drop'
)

#We convert our target variable (yes/no) into numerical values (1/0) because machine learning models require numeric inputs.
le = LabelEncoder()

le.fit(Y_train)

Y_train = le.transform(Y_train)
Y_test = le.transform(Y_test)
#We do label encoding on the target variable (Survived) to convert the categorical labels into numerical values. This is necessary because machine learning models typically require numerical input for training and prediction.

lr_model = Pipeline(
    steps=[
        ('preprocessor',preprocessor),
        ('model',LogisticRegression(class_weight='balanced',max_iter=1000))
    ]
)
"""
class_weight='balanced' means that the model will adjust the weights of the classes in the 
target variable to account for any class imbalance. 
This is important because if one class is much more prevalent than the other,
the model may be biased towards predicting that class more often,
leading to poor performance on the minority class.
"""

lr_model.fit(X_train,Y_train)

"""
lr_model['model'].coef_
it means we are accessing the coefficients of the logistic regression model that was 
trained on the training data.

lr_model['model'].intercept_
it means we are accessing the intercept of the logistic regression model that was
trained on the training data.


lr_model['model'].classes_
it means we are accessing the classes of the target variable that the logistic regression model 
was trained on.

So by using these three attributes, we can gain insights into how the model is 
making predictions and how it is separating the classes in the target variable.
"""

y_pred = lr_model.predict(X_test)

# Get the raw probability scores (e.g., 0.85 chance of death, 0.15 chance of survival)
print(lr_model.predict_proba(X_test))

accuracy = accuracy_score(Y_test,y_pred)
print(accuracy)
precision = precision_score(Y_test,y_pred)
print(precision)
recall = recall_score(Y_test,y_pred)
print(recall)
"""
precision lower means the model is making more false positive predictions, 
while a higher precision means the model is making fewer false positive predictions.

recall lower means the model is making more false negative predictions,
while a higher recall means the model is making fewer false negative predictions.

"""