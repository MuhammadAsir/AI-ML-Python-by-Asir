import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.datasets import load_breast_cancer
from sklearn.preprocessing import StandardScaler

from sklearn.decomposition import PCA



from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score


df=load_breast_cancer(as_frame=True).frame

X = df.drop('target',axis=1)
y = df['target']

scaler=StandardScaler()
X_scaled=scaler.fit_transform(X)

np.set_printoptions(suppress=True) #It means that we are setting the print options for numpy arrays to suppress scientific notation and display numbers in a more readable format.
pca_full=PCA(n_components=None) #none means we want to keep all the components

x_pca_full=pca_full.fit_transform(X_scaled)
#It means we are fitting the PCA model to the scaled data and transforming it into principal components.

explained_variance=pca_full.explained_variance_ratio_
#print("Explained Variance Ratio:",explained_variance) 
#It means we are getting the variance explained by each principal component.It works as a measure of how much information (variance) can be attributed to each of the principal components.

cum_explained_variance=np.cumsum(explained_variance)
#It means we are calculating the cumulative sum of the explained variance ratios, which gives us the total variance explained by the first n principal components.
print("Cumulative Explained Variance:",cum_explained_variance)

plt.plot(cum_explained_variance, marker='o')
plt.xlabel("Number of components")
plt.ylabel("Cumulative variance")
plt.grid()
plt.show()



X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.20, random_state=42, stratify=y
)

# Pipeline WITHOUT PCA: Scale -> Logistic Regression
pipe_no_pca = Pipeline([
    ("scaler", StandardScaler()),
    ("clf", LogisticRegression(max_iter=500))
])
#We didnt use ColumnTransformer because we are not using PCA here. We are just scaling the data and then applying logistic regression.
#We use column transformer when we want to apply different transformations to different columns of the data. In this case, we are applying the same transformation (scaling) to all columns, so we can use a simple pipeline.

pipe_no_pca.fit(X_train, y_train)
pred_no_pca = pipe_no_pca.predict(X_test)

acc_no_pca = accuracy_score(y_test, pred_no_pca)
print("Accuracy (No PCA):", acc_no_pca)


pipe_with_pca = Pipeline([
    ("scaler", StandardScaler()),
    ("pca", PCA(n_components=10)), #10 means we want to keep 10 components. We can also use a float value between 0 and 1 to specify the amount of variance we want to keep. For example, if we want to keep 95% of the variance, we can use n_components=0.95.
    ("clf", LogisticRegression(max_iter=500))
])

pipe_with_pca.fit(X_train, y_train)
pred_with_pca = pipe_with_pca.predict(X_test)

acc_with_pca = accuracy_score(y_test, pred_with_pca)
print("Accuracy (With PCA):", acc_with_pca)



"""
Explaination of the Results
If PCA accuracy is similar:

Great. We reduced dimensions without losing performance.
If PCA accuracy is better:

PCA likely removed redundancy/noise that was confusing the model.
If PCA accuracy is worse:

We removed useful information.
Increase the threshold (for example, 0.98), or skip PCA.
Bottom line: PCA is a tool. Use it when it matches the problem conditions.

"""