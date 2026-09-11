import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns 

from sklearn.model_selection import train_test_split
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OrdinalEncoder,OneHotEncoder,LabelEncoder,StandardScaler,MinMaxScaler
from sklearn.metrics import accuracy_score,confusion_matrix,classification_report,precision_score,recall_score,f1_score
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.model_selection import GridSearchCV
from sklearn.svm import SVC

df=pd.read_csv("titanic_data_updated.csv")

df['Family_Size'] = df['SibSp'] + df['Parch'] + 1
df['Cabin'] = df['Cabin'].fillna("Missing")

df['Deck'] = df['Cabin'].astype(str).str[0]

X = df.drop('Survived', axis=1)

# y contains only the survival status
y = df['Survived']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

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
categories = [['third','second','first']]

p3 = Pipeline(
    steps=[
        ('imputer',SimpleImputer(strategy='most_frequent')),
        ('encoder',OneHotEncoder(sparse_output=False,drop='first',handle_unknown='ignore'))
    ]
)

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

SVC_model = Pipeline(
    steps=[
        ('preprocessor',preprocessor),
        ('model',SVC())
    ]
)

grid_param =[ {
    "model__kernel" : ['linear'],
    "model__C" :[0.01 , 0.1 , 1 , 10 , 50 , 100]
},
  {
      "model__kernel" : ['rbf'] ,
      "model__C" :[0.01 , 0.1 ,1,100],
      "model__gamma" :[0.01,0.1,5,10,'scale','auto']
  },
    {
        "model__kernel": ['poly'],
        "model__C" :[0.01 , 0.1 , 1 ,100],
        "model__degree" : [2,3]
    }

]
"""
1. Linear Kernel
--------------------------------------------------

{
    "model__kernel": ['linear'],
    "model__C": [0.01, 0.1, 1, 10, 50, 100]
}

Explanation:
- Use the Linear kernel.
- Try six different values of C.
- Since the Linear kernel does not use gamma or degree, only C is tested.

Combinations:
6

--------------------------------------------------
2. RBF Kernel
--------------------------------------------------

{
    "model__kernel": ['rbf'],
    "model__C": [0.01, 0.1, 1, 100],
    "model__gamma": [0.01, 0.1, 5, 10, 'scale', 'auto']
}

Explanation:
- Use the RBF kernel.
- Try four values of C.
- For each C, try six values of gamma.

What is gamma?
- Gamma controls how much influence a single training point has.
- Small gamma → Smooth decision boundary.
- Large gamma → More complex decision boundary (may overfit).

Combinations:
4 × 6 = 24

--------------------------------------------------
3. Polynomial Kernel
--------------------------------------------------

{
    "model__kernel": ['poly'],
    "model__C": [0.01, 0.1, 1, 100],
    "model__degree": [2, 3]
}

Explanation:
- Use the Polynomial kernel.
- Try four values of C.
- Try polynomial degree 2 and 3.

What is degree?
- Degree controls the complexity of the polynomial.
- Degree = 2 → Quadratic boundary.
- Degree = 3 → Cubic boundary.

Combinations:
4 × 2 = 8

"""

best_SVC_model = GridSearchCV(
    estimator = SVC_model ,
    param_grid = grid_param , 
    cv = 5
    )

best_SVC_model.fit(X_train,y_train)
y_pred_train = best_SVC_model.predict(X_train)

print(accuracy_score(y_train,y_pred_train))
y_pred = best_SVC_model.predict(X_test)

accuracy = accuracy_score(y_test,y_pred)
print(accuracy)
precision = precision_score(y_test,y_pred)
print(precision)
