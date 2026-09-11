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

"""
Random Forests combine many decision trees to make a more stable prediction. 
We use Grid Search again to find the optimal number of trees (`n_estimators`) and 
feature selection strategies.
Random Forest-> low bias and low variance. 
It is a good model to use when you have a lot of features and want to avoid overfitting.

In a Decision Tree, changing a few data points can completely change the tree structure. 
In a Random Forest, only some individual trees may change because each tree 
uses random samples and random features, 
while the final prediction is usually stable due to majority voting.

Why does averaging predictions in Random Forest regression reduce variance?
->Because averaging cancels out individual tree errors that are not perfectly correlated

"""

df = load_breast_cancer(as_frame=True).frame

X = df.drop(['target'],axis=1)
y = df['target']
X_train , X_test,y_train,y_test = train_test_split(X,y,test_size=0.2,random_state=42,stratify=y)

#We will use random forest classifier for classification problem and will use regressor for regression problem. We will use Grid Search to find the optimal hyperparameters for both models.

grid_param={
    "n_estimators" : [100,150,200],
    "criterion" : ['gini','entropy'],
    "max_features" : ['sqrt','log2'],
}
#n_estimators: The number of trees in the forest. More trees usually lead to better performance, but also increase computation time.
#max_features: The number of features to consider when looking for the best split. 'sqrt' means square root of the total number of features, 'log2' means logarithm base 2 of the total number of features.

grid_search_RF = GridSearchCV(
    estimator = RandomForestClassifier(),
    param_grid = grid_param,
    cv = 5
)

grid_search_RF.fit(X_train,y_train)

#training data accuracy for RF
y_pred_train = grid_search_RF.predict(X_train)
print(f"Training Accuracy: {accuracy_score(y_train,y_pred_train)}")


# testing accuracy
y_pred = grid_search_RF.predict(X_test)

print(f"Testing Accuracy: {accuracy_score(y_test,y_pred)}")

#So Random forest performing better than a single decision tree. We can also check the feature importance to see which features are more important for the model.