"""

# Support Vector Machine (SVM) - Quick Notes


1. What is Support Vector Machine (SVM)?
------------------------------------------------------------

Support Vector Machine (SVM) is a supervised machine learning algorithm used for:

- Classification
- Regression (SVR)

However, SVM is mainly used for classification problems.

The main goal of SVM is to find the best boundary (called a hyperplane) that separates different classes.

------------------------------------------------------------

2. What is a Hyperplane?
------------------------------------------------------------

A hyperplane is the decision boundary that separates different classes.

Example (2D):

        Class A (●)

      ●      ●

---------------------------  <- Hyperplane

                ○      ○

             Class B (○)

The hyperplane is chosen so that the distance between the two classes is as large as possible.

------------------------------------------------------------

3. What are Support Vectors?
------------------------------------------------------------

Support Vectors are the data points that are closest to the hyperplane.

These points are the most important because they determine the position of the hyperplane.

Example:

      ●       ●
          ●

---------------------- Hyperplane

          ○
      ○       ○

The closest points (● and ○) are called Support Vectors.

If these points move, the hyperplane also changes.

------------------------------------------------------------

4. What is Margin?
------------------------------------------------------------

Margin is the distance between the hyperplane and the nearest support vectors.

SVM tries to maximize this margin.

Hinge loss is a loss function used in SVM to ensure that the margin is maximized.
Formula of Hinge Loss: max(0, 1 - Yi * (Xi * W + b))
So it is used to penalize the points that are on the wrong side of the margin.
if hinge loss is 0, it means the point is correctly classified and on the right side of the margin.
if hinge loss is greater than 0, it means the point is either on the wrong side of the margin or misclassified.

Hard Margin(perfectionist): If the data is linearly separable, SVM can create a hard margin, which means that all points are correctly classified and there are no points inside the margin.

Soft Margin(Realistic): If the data is not linearly separable, SVM can create a soft margin, which means that some points can be misclassified or inside the margin.

In one sentence:
Hard Margin: No misclassification allowed.
Soft Margin: A few misclassifications are allowed to achieve better overall performance.

Large Margin
-------------
Better generalization
Less overfitting

Small Margin
-------------
Higher chance of overfitting

------------------------------------------------------------

5. Goal of SVM
------------------------------------------------------------

Find the hyperplane that:

✓ Maximizes the margin

✓ Correctly classifies the data

This is called the Maximum Margin Classifier.

------------------------------------------------------------

6. How Does SVM Work?
------------------------------------------------------------

Step 1:
Take the training data.

↓

Step 2:
Find all possible hyperplanes.

↓

Step 3:
Calculate the margin for each hyperplane.

↓

Step 4:
Choose the hyperplane with the largest margin.

↓

Step 5:
Use this hyperplane to classify new data.

------------------------------------------------------------

7. Linear SVM
------------------------------------------------------------

Used when the data can be separated using a straight line.

Example:

● ● ● ●

----------------------

○ ○ ○ ○

A straight line can perfectly separate the classes.

------------------------------------------------------------

8. Non-Linear SVM
------------------------------------------------------------

Sometimes the data cannot be separated using a straight line.

Example:

        ○ ○ ○
      ○ ● ● ○
      ○ ● ● ○
        ○ ○ ○

Here, a straight line cannot separate the classes.

SVM uses the Kernel Trick to transform the data into a higher-dimensional space where it becomes linearly separable.

------------------------------------------------------------

9. What is a Kernel?
------------------------------------------------------------

A Kernel is a mathematical function that transforms data into a higher-dimensional space so that it becomes easier to separate.

Common kernels:

1. Linear Kernel
   - Used for linearly separable data.

2. Polynomial Kernel
   - Creates curved decision boundaries.

3. RBF (Radial Basis Function) Kernel
   - Most commonly used.
   - Handles complex, non-linear data.

4. Sigmoid Kernel
   - Similar to a neural network activation function.

------------------------------------------------------------

10. Advantages of SVM
------------------------------------------------------------

✓ High accuracy

✓ Works well with high-dimensional data

✓ Effective for small and medium-sized datasets

✓ Less prone to overfitting because of the maximum margin

✓ Works well when features are greater than samples

------------------------------------------------------------

11. Disadvantages of SVM
------------------------------------------------------------

✗ Slow for very large datasets

✗ Choosing the right kernel can be difficult

✗ Sensitive to noisy data and outliers

✗ Hard to interpret compared to Decision Trees

------------------------------------------------------------

12. Decision Tree vs Random Forest vs SVM
------------------------------------------------------------

Decision Tree
-------------
- Single tree
- Easy to understand
- Can overfit easily
- Fast

Random Forest
-------------
- Many trees
- More accurate
- Less overfitting
- Harder to interpret

Support Vector Machine
----------------------
- Finds the best hyperplane
- Uses support vectors
- Maximizes the margin
- Very effective for high-dimensional data
- Can handle non-linear data using kernels

------------------------------------------------------------

13. Important Terms
------------------------------------------------------------

Hyperplane
-----------
The decision boundary that separates different classes.

Support Vectors
---------------
The closest data points to the hyperplane.

Margin
------
Distance between the hyperplane and the nearest support vectors.

Kernel
------
A function that transforms data into a higher-dimensional space for better separation.

------------------------------------------------------------

14. When Should You Use SVM?
------------------------------------------------------------

Use SVM when:

✓ Dataset is small or medium-sized

✓ Number of features is high

✓ Classes are clearly separable

✓ You need high classification accuracy

Avoid SVM when:

✗ Dataset is extremely large

✗ Training speed is very important

✗ The dataset contains many noisy samples or outliers

------------------------------------------------------------

15. Interview Summary
------------------------------------------------------------

Support Vector Machine (SVM) is a supervised learning algorithm mainly used for classification. It finds the best hyperplane that separates different classes while maximizing the margin between them. The closest data points to the hyperplane are called support vectors. For non-linearly separable data, SVM uses kernel functions such as Linear, Polynomial, and RBF to transform the data into a higher-dimensional space, making it easier to separate.

------------------------------------------------------------

16. Easy Way to Remember
------------------------------------------------------------

Decision Tree
-------------
"Keep splitting the data."

Random Forest
-------------
"Combine many Decision Trees."

Support Vector Machine
----------------------
"Find the best boundary with the maximum margin."

Support Vectors
---------------
"The nearest points that decide the boundary."

Margin
------
"The larger the margin, the better the model usually generalizes."

Kernel
------
"Transforms data so that even complex patterns can be separated."

"""