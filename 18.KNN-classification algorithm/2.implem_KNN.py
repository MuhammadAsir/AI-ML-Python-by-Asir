import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline

from sklearn.datasets import load_wine

from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score,precision_score,recall_score

from sklearn.metrics import confusion_matrix,classification_report

df = load_wine(as_frame=True).frame

print(df.sample(5))

sns.countplot(data= df , x='target')
plt.show()

X = df.drop(['target'],axis=1)
y = df['target']

X_train , X_test,y_train,y_test = train_test_split(X,y,test_size=0.2,random_state=42,stratify=y)

knn_model = Pipeline(
    steps=[
        ('scaler',StandardScaler()),
        ('model',KNeighborsClassifier(n_neighbors=15,metric='minkowski',p=2))
    ]
)


#metrice='minkowski' means Euclidean distance and p=2 means the order of the norm (Euclidean norm).

knn_model.fit(X_train,y_train)
# we know knn dont require training phase but we fit the model to store the training data and prepare for prediction.
y_pred = knn_model.predict(X_test)

accuracy = accuracy_score(y_test,y_pred)
print(accuracy)

conf_mat = confusion_matrix(y_test,y_pred)
print(conf_mat)

print(classification_report(y_test,y_pred))

#Hyperparameter Tuning & Error Analysis:
"""
To find the optimal value for k, we iterate through a range of neighbors and 
compare the performance using different distance metrics (Euclidean vs. Manhattan)."""

#Case 1: Minkowski Distance (p=2, Euclidean)
euc_performance = [] 
euc_acc=[]

for k in range(5,30):
    knn_model = Pipeline(
        steps=[
            ('scaler',StandardScaler()),
            ('model',KNeighborsClassifier(n_neighbors=k,metric='minkowski',p=2))
        ]
    )
    knn_model.fit(X_train,y_train)
    y_pred = knn_model.predict(X_test)
    score = accuracy_score(y_test,y_pred)
    euc_acc.append(score)
    euc_performance.append({
        'k': k,
        'accuracy': score,
        'precision': precision_score(y_test, y_pred, average='weighted', zero_division=0),
        'recall': recall_score(y_test, y_pred, average='weighted', zero_division=0)
    })

plt.figure(figsize=(10, 5))
plt.plot(range(5, 30), euc_acc)
plt.title('Accuracy vs. K Value (Euclidean Distance)')
plt.xlabel('Number of Neighbors (K)')
plt.ylabel('Test Accuracy')
plt.grid(True)
plt.show()

#Case 2: Minkowski Distance (p=1, Manhattan)

manhattan_performance = []
manhattan_acc = []

for k in range(5, 30):
    knn_pipeline = Pipeline(steps=[
        ('scaler', StandardScaler()),
        ('model', KNeighborsClassifier(n_neighbors=k, metric='minkowski', p=1))
    ])
    knn_pipeline.fit(X_train, y_train)
    y_pred = knn_pipeline.predict(X_test)

    score = accuracy_score(y_test, y_pred)
    manhattan_acc.append(score)
    manhattan_performance.append({
        'k': k,
        'accuracy': score,
        'precision': precision_score(y_test, y_pred, average='weighted', zero_division=0),
        'recall': recall_score(y_test, y_pred, average='weighted', zero_division=0)
    })


plt.figure(figsize=(10, 5))
plt.plot(range(5, 30), manhattan_acc, marker='o', linestyle='--', color='r')
plt.title('Accuracy vs. K Value (Manhattan Distance)')
plt.xlabel('Number of Neighbors (K)')
plt.ylabel('Test Accuracy')
plt.grid(True)
plt.show()