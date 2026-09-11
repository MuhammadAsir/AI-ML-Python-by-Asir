import numpy as np 
import pandas as pd

import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans


df = load_iris(as_frame=True).frame
X = df[['sepal length (cm)','sepal width (cm)']]

scaler=StandardScaler()
x_scaled=scaler.fit_transform(X) 
#We don't need train-test split for unsupervised learning, as we are not predicting any target variable.

k_means=KMeans(n_clusters=3, random_state=42,max_iter=400,init='k-means++')
#init='k-means++' is a method for initializing the centroids before running the K-Means algorithm. It helps to speed up convergence and improve the quality of the final clusters.
k_means.fit(x_scaled)

df['clusters'] =k_means.labels_ #It assigns the cluster labels to the original DataFrame.
sns.scatterplot( 
    x = df['sepal length (cm)'],
    y = df['sepal width (cm)'],
    hue = df['clusters'],
    palette = 'viridis')
#palatte='viridis' is a color map that provides a visually appealing gradient of colors for the clusters in the scatter plot.
plt.title("K Means Clustering")
plt.xlabel("Sepal length")
plt.ylabel("Sepal width")
plt.show()

print(f"Inertia: {k_means.inertia_}")

"""
What is Inertia?
Inertia in K-Means clustering is like a measure of how 'tight' or 'compact' our clusters are. 
Think of it as the sum of how far each point is from the center of its own cluster. 
A smaller inertia value means that the points within each cluster are 
generally closer to their cluster's center, which usually suggests a better clustering result. 
However, it's important to remember that inertia will always decrease as you add more clusters,
so we often use it with other methods to find the best number of clusters.

Inertia vs. SSE (Sum of Squared Errors)
Is Inertia similar to SSE? Yes, they are the exact same thing!


In the context of K-Means:

SSE stands for Sum of Squared Errors. It calculates the error by 
squaring the distance between each point and its assigned cluster center.
Inertia is simply the name that the scikit-learn library (and the K-Means algorithm in general) 
uses for that SSE value.
So, if your teacher asks for the 'SSE' of your clusters, you can just look at the 
inertia_ value! Both tell you how much the data points 'deviate' from their centers.

"""