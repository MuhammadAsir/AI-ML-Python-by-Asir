import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split


from sklearn.datasets import load_breast_cancer

from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier


from sklearn.metrics import accuracy_score,precision_score,recall_score

from sklearn.metrics import confusion_matrix,classification_report

from sklearn.model_selection import GridSearchCV

df = load_breast_cancer(as_frame=True).frame

X=df.drop(['target'],axis=1)
y=df['target']
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

#Training on different depths---------------
model_1 = DecisionTreeClassifier(max_depth=2)

model_1.fit(X_train,y_train)
# training data accuracy
y_pred_train = model_1.predict(X_train)
print(f"Training Accuracy: {accuracy_score(y_train,y_pred_train)}")


# testing accuracy
y_pred = model_1.predict(X_test)

print(f"Testing Accuracy: {accuracy_score(y_test,y_pred)}")

model_2 = DecisionTreeClassifier(max_depth=3)

model_2.fit(X_train,y_train)

# training data accuracy
y_pred_train = model_2.predict(X_train)
print(f"Training Accuracy: {accuracy_score(y_train,y_pred_train)}")


# testing accuracy
y_pred = model_2.predict(X_test)

print(f"Testing Accuracy: {accuracy_score(y_test,y_pred)}")

model_3 = DecisionTreeClassifier(max_depth=4)

model_3.fit(X_train,y_train)

# training data accuracy
y_pred_train = model_3.predict(X_train)
print(f"Training Accuracy: {accuracy_score(y_train,y_pred_train)}")


# testing accuracy
y_pred = model_3.predict(X_test)

print(f"Testing Accuracy: {accuracy_score(y_test,y_pred)}")

#model 1,2,3 has overfitting cz we can see training accuracy is very high and testing accuracy is low. So we can say that model is overfitting.

#grid search
# training data accuracy
y_pred_train = grid_search.predict(X_train)
print(f"Training Accuracy: {accuracy_score(y_train,y_pred_train)}")


# testing accuracy
y_pred = grid_search.predict(X_test)

print(f"Testing Accuracy: {accuracy_score(y_test,y_pred)}")

#Grid search model also giving high training accuracy and low testing accuracy. So we can say that model is overfitting.