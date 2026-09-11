"""

PCA
===

PCA stands for Principal Component Analysis.

PCA is an unsupervised learning technique used for
dimensionality reduction.

The main idea of PCA is:

"Reduce the number of features while keeping as much
important information as possible."


WHY DO WE NEED PCA?
===================

PCA is useful when a dataset has many features.

Problems with many features:

1. Training can become slower.
2. Data becomes difficult to visualize.
3. Some features may contain similar information.
4. High-dimensional data can cause problems.
5. Models can become more complex.

Example:

100 features
     |
    PCA
     |
10 principal components

PCA reduces the number of dimensions.


WHAT IS A PRINCIPAL COMPONENT?
==============================

A Principal Component is a new feature created by
combining the original features.

The components are ordered based on how much information
(or variance) they capture.

PC1 -> Captures the most variance
PC2 -> Captures the second most variance
PC3 -> Captures the third most variance
...


HOW DOES PCA WORK?
==================

1. Collect the dataset.

2. Scale the features.

3. Find the directions with maximum variance.

4. Create new axes called Principal Components.

5. Rank the components based on the amount of variance
   they capture.

6. Select the most important components.

7. Transform the original data into the new
   lower-dimensional data.


EXAMPLE
=======

Suppose we have:

10 features
    |
    PCA
    |
3 Principal Components

PC1 -> 60% variance
PC2 -> 25% variance
PC3 -> 10% variance

Total = 95% variance

So, we can keep the 3 components and remove the
remaining information.


WHY DO WE SCALE BEFORE PCA?
===========================

PCA is affected by the scale of features.

Example:

Age       -> 20 - 60
Salary    -> 20,000 - 500,000

Salary has much larger values.

Therefore, we normally scale the data before PCA.

Commonly used:

StandardScaler()


ADVANTAGES OF PCA
=================

1. Reduces the number of features.

2. Makes high-dimensional data easier to visualize.

3. Can make machine learning training faster.

4. Removes redundant information.

5. Can reduce noise.

6. Helps with high-dimensional datasets.


DISADVANTAGES OF PCA
====================

1. Principal components are difficult to interpret.

2. Some information can be lost.

3. Features usually need to be scaled first.

4. PCA is sensitive to outliers.

5. Choosing the number of components can be difficult.

6. Original feature meanings may be lost.


PCA VS FEATURE SELECTION
========================

Feature Selection:

10 features
     |
   Select
     |
3 original features


PCA:

10 features
     |
    PCA
     |
3 new Principal Components


Feature Selection:
Keeps some of the original features.

PCA:
Creates new features from the original features.


WHEN SHOULD WE USE PCA?
=======================

Use PCA when:

1. The dataset has many features.

2. Features contain redundant information.

3. You want to visualize high-dimensional data.

4. You want to reduce computational complexity.

5. You want to reduce dimensionality.


EASY WAY TO REMEMBER
====================

PCA = Dimensionality Reduction

PCA tries to:

"Keep the important information
while reducing the number of features."


SIMPLE EXAMPLE
==============

Original:

100 features
     |
     PCA
     |
10 Principal Components

Instead of working with 100 features,
we work with only 10 important components.


"""