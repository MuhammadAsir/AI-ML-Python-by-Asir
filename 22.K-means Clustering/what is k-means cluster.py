"""
What is K-Means Clustering?

K-Means Clustering is an unsupervised machine learning algorithm that automatically groups 
similar data points into K clusters.

K = Number of clusters you want.
Means = The center (average position), called the centroid, of each cluster.

Unlike supervised learning, K-Means does not need labeled data. 
It finds hidden patterns based only on the similarity between data points.

Why Do We Need K-Means Clustering? 
Imagine you have a dataset of customer information, 
and you want to segment your customers into different groups based on their purchasing behavior. 
K-Means Clustering can help you identify these groups without any prior knowledge of the labels.

How it Works:
1. Choose the number of clusters (K) you want to create.
2. Randomly initialize K centroids (the center points of the clusters).
3. Assign each data point to the nearest centroid, forming K clusters.
4. Recalculate the centroids of the newly formed clusters.
5. Repeat steps 3 and 4 until the centroids no longer change significantly or a maximum number of iterations is reached.

Real-World Applications of K-Means Clustering:
1. Customer Segmentation: Grouping customers based on purchasing behavior for targeted marketing.
2. Image Compression: Reducing the number of colors in an image by clustering similar colors.
3. Anomaly Detection: Identifying unusual data points that do not fit into any cluster.

Advantages of K-Means Clustering:
Simple and easy to understand.
Fast, even for large datasets.
Works well when clusters are compact and roughly spherical.
Easy to implement.
Widely used in business, healthcare, finance, and marketing.

Disadvantages of K-Means Clustering:

You must choose K beforehand.
Sensitive to the initial random centroids.
Does not work well when clusters have irregular shapes.
Sensitive to outliers.
Works best with numerical data.












"""