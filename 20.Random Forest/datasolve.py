import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.impute import SimpleImputer
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OrdinalEncoder,OneHotEncoder,LabelEncoder,StandardScaler,MinMaxScaler
from sklearn.pipeline import Pipeline
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import GridSearchCV


df=pd.read_csv("heart_disease_uci.csv")

df.duplicated().sum()
df.drop_duplicates(inplace=True)
df.isnull().sum()

df['num'] = df['num'].apply(lambda x: 1 if x > 0 else 0)
df.drop('id', axis=1, inplace=True)

nominal_cat = ['sex', 'dataset', 'cp', 'fbs', 'restecg', 'exang', 'slope', 'thal']

numerical_col = ['age', 'trestbps', 'chol', 'thalch', 'oldpeak', 'ca']

numerical_transformers = Pipeline(
    steps=[
        ('imputer', SimpleImputer(strategy='median'))
       
    ]
)
nominal_transformers = Pipeline(
    steps=[
        ('imputer', SimpleImputer(strategy='most_frequent')),
        ('encoder', OneHotEncoder(sparse_output=False, handle_unknown="ignore"))
    ]
)

preprocessor = ColumnTransformer(
    transformers=[
        ('numerical', numerical_transformers, numerical_col),
        ('nominal', nominal_transformers, nominal_cat)
    ],
    remainder='passthrough',
)

x = df.drop(['num'], axis=1)
y = df['num']

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42,stratify=y)

rf_pipe = Pipeline([
    ("preprocessor", preprocessor),
    ("model", RandomForestClassifier(random_state=42, class_weight="balanced"))
])

param_grid = {
    "model__n_estimators": [100, 200, 300],
    "model__criterion": ["gini", "entropy"],
    "model__max_depth": [None, 10, 20],
    "model__min_samples_split": [2, 5],
    "model__min_samples_leaf": [1, 2],
    "model__max_features": ["sqrt", "log2"]
}

grid_search_RF = GridSearchCV(
    estimator=rf_pipe,
    param_grid=param_grid,
    cv=5,
    scoring="accuracy",
    n_jobs=-1
)

grid_search_RF.fit(x_train, y_train)

best_model = grid_search_RF.best_estimator_

train_pred = best_model.predict(x_train)

print("Training Accuracy:",
      accuracy_score(y_train, train_pred))

test_pred = best_model.predict(x_test)

print("Testing Accuracy:",
      accuracy_score(y_test, test_pred))

print(confusion_matrix(y_test, test_pred))