import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split


from sklearn.datasets import load_iris

from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score,precision_score,recall_score

from sklearn.metrics import confusion_matrix,classification_report

from sklearn.model_selection import GridSearchCV

#We don't need scaling and pipeline for Decision Tree Classifier as it is not affected by scaling and pipelining.

df = load_iris(as_frame=True).frame

X = df.drop(['target'],axis=1)
y = df['target']
X_train , X_test,y_train,y_test = train_test_split(X,y,test_size=0.2,random_state=42,stratify=y)

model = DecisionTreeClassifier()

model.fit(X_train,y_train)

y_pred = model.predict(X_test)

print(classification_report(y_test,y_pred))

grid = {
    "criterion" : ['gini','entropy'],
    "max_depth" :[1,2,3,4,5,6,7,8,None],
}

grid_search = GridSearchCV(
    estimator = model,
    param_grid = grid,
    cv = 5
)

grid_search.fit(X_train,y_train)

y_pred = grid_search.predict(X_test)

print(classification_report(y_test,y_pred))

