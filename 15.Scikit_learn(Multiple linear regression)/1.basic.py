import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.impute import SimpleImputer
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OrdinalEncoder,OneHotEncoder,LabelEncoder,StandardScaler,MinMaxScaler
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LinearRegression,SGDRegressor
from sklearn.metrics import mean_squared_error,r2_score,root_mean_squared_error,mean_absolute_error

df = pd.read_csv("bangladesh_student_performance_updated.csv")
df.isnull().sum()
print(df.isnull().sum())
#EDA:-
df.duplicated().sum()
df.drop_duplicates(inplace=True)

# Generate histograms for all numerical features to visualize their distributions
# 'bins=15' controls the number of bars, and 'figsize' sets the display dimensions
df.hist(bins=15, figsize=(10, 6))
#figsize=(10,6) means the width of the plot will be 10 inches and the height will be 6 inches. This helps to make the plots more readable and visually appealing.

plt.title("Distribution of Numerical Features")
plt.show()

numerical_cols = ['age','tuition_fee','ssc_result','hsc_result']


plt.figure(figsize=(8,6))

sns.heatmap(df[numerical_cols].corr(),
                 annot=True, 
                 cmap='coolwarm', 
                 linewidths=0.5)

#annot=true adds the correlation values to the heatmap, cmap='coolwarm' sets the color scheme, and linewidths=0.5 adds lines between the cells for better visibility.

plt.title("Correlation Heatmap of Numerical Columns")
plt.show()

sns.boxplot(data=df , x="ssc_result")
plt.show()

"""preprocessing:
Preprocessing is a critical step where we handle missing values, 
encode categorical variables (nominal and ordinal),
and scale numerical features to prepare them for the machine learning models.
"""

nominal_cat = ['gender','address','famsize','Pstatus','relationship','smoker','F_Job','M_Job']

# Numerical columns: continuous values that require scaling and imputation
numerical_col = ['age','tuition_fee','ssc_result']

#ML Pipeline:Imputation and Scaling for numerical features, and encoding for categorical features
"""
Imputing → Fill missing values.
Encoding → Convert text to numbers.
Scaling → Adjust number ranges.
"""


numerical_transformers = Pipeline(
    steps=[
        ('imputer', SimpleImputer(strategy='mean')),
        ('scaler', StandardScaler())
    ]
)

nominal_transformers = Pipeline(
    steps=[
        ('imputer', SimpleImputer(strategy='most_frequent')),
        ('encoder', OneHotEncoder(sparse_output=False, handle_unknown="ignore"))
    ]
)
"""
Raw Data
   ↓
[ Step 1: Clean (Imputer) ]
   ↓
[ Step 2: Convert (Encoder) ]
   ↓
Final Output
"""


preprocessor = ColumnTransformer(
    transformers=[
        ('numerical', numerical_transformers, numerical_col),
        ('nominal', nominal_transformers, nominal_cat)
    ],
    remainder='passthrough',
)

# Split features (X) and target (y)
x = df.drop(['date', 'hsc_result'], axis=1)
y = df['hsc_result']

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

#LinearRegression 
# Initialize the Linear Regression pipeline
# This combines our preprocessing steps with the Linear Regression algorithm
Lr_pipe=Pipeline(
    steps=[
        ('preprocessor',preprocessor),
        ('model' , LinearRegression())
    ]
)
"""
This pipeline means:
Take raw data, preprocess it automatically, 
then feed it into Linear Regression for training and prediction.”
"""

Lr_pipe.fit(x_train,y_train) # Train the model on the training data
Lr_pipe.predict(x_test)

# Initialize the Stochastic Gradient Descent (SGD) Regressor pipeline
# SGD is an optimization technique often used for large-scale learning
SGD_pipe=Pipeline(
    steps=[
        ('preprocessor',preprocessor),
        ('model' , SGDRegressor())
    ]
)

# Train the SGD model
SGD_pipe.fit(x_train,y_train)
SGD_pipe.predict(x_test)


"""
MAE,MSE,RMSE,R² → evaluation metrics to measure how well our model is performing.

Think like a teacher grading a student:
MAE → average marks lost
MSE → harsh penalty for big mistakes
RMSE → actual mistake level
R² → how good student is overall


Error metrics (MAE, MSE, RMSE):
👉 Smaller = better

R² score:
👉 Bigger = better

"""

y_pred = Lr_pipe.predict(x_test)

# Calculate and print performance metrics
# MSE/RMSE: measure error magnitude; R2: measures explained variance; MAE: measures average error
print(f"MSE: {round(mean_squared_error(y_test, y_pred), 4)}")
print(f"R2: {round(r2_score(y_test, y_pred), 4)}")
print(f"RMSE: {round(root_mean_squared_error(y_test, y_pred), 4)}")
print(f"MAE: {round(mean_absolute_error(y_test, y_pred), 4)}")

print('\n')
# --- SGD Regression Evaluation ---
# Predict HSC results using the SGD model
y_pred = SGD_pipe.predict(x_test)

# Compare these results with the standard Linear Regression model
print(f"MSE: {round(mean_squared_error(y_test, y_pred), 4)}")
print(f"R2: {round(r2_score(y_test, y_pred), 4)}")
print(f"RMSE: {round(root_mean_squared_error(y_test, y_pred), 4)}")
print(f"MAE: {round(mean_absolute_error(y_test, y_pred), 4)}")

print(x_train.isnull().sum())