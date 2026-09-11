"""
DBSCAN
======

DBSCAN stands for:
Density-Based Spatial Clustering of Applications with Noise.

DBSCAN is an unsupervised learning algorithm used for clustering.

It groups points that are closely packed together and
identifies isolated points as noise/outliers.


WHY DO WE NEED DBSCAN?
======================

K-Means has some limitations:

1. We need to specify the number of clusters (K).
2. It does not work well with irregular-shaped clusters.
3. It does not directly detect outliers.

DBSCAN solves these problems by using density.

DBSCAN can:
- Find clusters without knowing the number of clusters.
- Find irregular-shaped clusters.
- Detect noise and outliers.


HOW DOES DBSCAN WORK?
=====================

DBSCAN mainly uses two parameters:

1. eps
   - Maximum distance between two points to be considered neighbors.

2. min_samples
   - Minimum number of points required to form a dense region.


TYPES OF POINTS
===============

1. Core Point
   - A point that has at least min_samples points
     within the eps distance.

2. Border Point
   - A point that does not have enough neighbors itself,
     but is close to a core point.

3. Noise Point
   - A point that does not belong to any cluster.
   - It is considered an outlier.


WORKING STEPS
=============

1. Select a point.

2. Find all points within the eps distance.

3. Count the neighboring points.

4. If the number of neighbors >= min_samples:
   - The point becomes a Core Point.
   - A new cluster is created.

5. DBSCAN expands the cluster by checking neighboring points.

6. If a point is close to a core point but does not have
   enough neighbors itself:
   - It becomes a Border Point.

7. If a point does not belong to any cluster:
   - It becomes a Noise Point.


ADVANTAGES
==========

1. No need to specify the number of clusters.

2. Can find irregular-shaped clusters.

3. Can detect outliers and noise.

4. Does not require centroids.

5. Works well when clusters have similar density.


DISADVANTAGES
=============

1. Choosing eps can be difficult.

2. Choosing min_samples can be difficult.

3. Does not work well when clusters have very different densities.

4. Sensitive to feature scaling.

5. Can struggle with high-dimensional data.

6. Poor parameter selection can produce bad clusters.

7. Won't work well in open spaces with varying densities.


DBSCAN vs K-MEANS
=================

K-Means:
- Requires number of clusters (K).
- Uses centroids.
- Works best with spherical/round clusters.
- Does not directly detect outliers.

DBSCAN:
- Does not require number of clusters.
- Does not use centroids.
- Can find irregular-shaped clusters.
- Can detect outliers.
- Uses density to form clusters.


WHEN TO USE DBSCAN
==================

Use DBSCAN when:

- You don't know the number of clusters.
- Your clusters have irregular shapes.
- Your dataset contains outliers.
- Your data forms dense groups.
- You want to identify noise automatically.


IMPORTANT
=========

DBSCAN = Density-Based Clustering

eps = Neighborhood distance

min_samples = Minimum points needed for a dense region

Core Point = Dense point

Border Point = Point near a core point

Noise Point = Outlier


SIMPLE MEMORY TRICK
===================

DBSCAN looks for:

"Crowded areas = Clusters"

"People near the crowd = Border Points"

"People standing alone = Noise"

"""