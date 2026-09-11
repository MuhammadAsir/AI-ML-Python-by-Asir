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

from sklearn.model_selection import GridSearchCV
from sklearn.metrics import classification_report, confusion_matrix


df = load_wine(as_frame=True).frame
X = df.drop(['target'],axis=1)
y = df['target']

X_train , X_test,y_train,y_test = train_test_split(X,y,test_size=0.2,random_state=42,stratify=y)

knn_model = Pipeline(
    steps=[
        ('scaler',StandardScaler()),
        ('knn',KNeighborsClassifier())
    ]
)
knn_model.fit(X_train,y_train)

#Hyperparameter Tuning
"""
We define a parameter grid to optimize the number of neighbors, the weight function,
and the power parameter for the Minkowski metric. GridSearchCV is used with 5-fold cross-validation
to find the most effective configuration."""

grid = {
    "knn__n_neighbors" : [3,5,7,11,13,17],
    "knn__weights" :['uniform','distance'],
    "knn__p" : [1,2]
}

grid_search = GridSearchCV(
    estimator = knn_model,
    param_grid = grid,
    cv = 5
)
#estimator means the model we want to tune, param_grid is the dictionary of hyperparameters we want to search over, and cv is the number of folds for cross-validation.

grid_search.fit(X_train,y_train)

print(grid_search.best_params_)
print(grid_search.best_estimator_)

#Model Evaluation
"""We utilize the best estimator to make predictions on the unseen test set 
and evaluate the performance using accuracy metrics"""

model = grid_search.best_estimator_

y_pred= model.predict(X_test)
accuracy = accuracy_score(y_test,y_pred)
print(accuracy)


# Display detailed classification metrics
print("Classification Report:")
print(classification_report(y_test, y_pred))

# Visualize the results with a Confusion Matrix
plt.figure(figsize=(8,6))
sns.heatmap(confusion_matrix(y_test, y_pred), annot=True, fmt='d', cmap='Blues')
#annot=true means that the values will be displayed in the cells, fmt='d' means that the values will be formatted as integers, and cmap='Blues' specifies the color map for the heatmap.
plt.title('Confusion Matrix: Wine Classification')
plt.show()


