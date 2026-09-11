"""
# K-Nearest Neighbors (KNN)

## What is KNN?

KNN (K-Nearest Neighbors) is a **Supervised Machine Learning algorithm** used for both:

- Classification
- Regression

It predicts the output by looking at the **K closest data points (neighbors)** in the 
training dataset.

Unlike Logistic Regression, KNN **does not learn a mathematical model**. 
It simply stores the training data and makes predictions when new data arrives.

## How KNN Works

1. Choose a value for **K**.
2. Calculate the distance between the new data point and every training sample.
3. Sort the distances.
4. Select the K nearest neighbors.
5. **Classification:** Choose the majority class.
6. **Regression:** Take the average of the neighbors' values.


## What is K?

K = Number of nearest neighbors considered.

Example:

K = 3

```
Yes
Yes
No
```

Prediction = **Yes** (majority vote)

---

# Distance Metric

A **Distance Metric** measures how similar or different two data points are.

- Smaller distance → More similar
- Larger distance → Less similar

KNN uses distance metrics to find the nearest neighbors.

---

# Euclidean Distance

The straight-line distance between two points.

Formula:

d = √((x₂-x₁)² + (y₂-y₁)²)

Use when:
- Numerical data
- Continuous features
- Most ML problems

Example:

A(2,3)

B(5,7)

Distance = √((5-2)² + (7-3)²)

= √25

= 5

---

# Manhattan Distance

The distance traveled only horizontally and vertically.

Formula:

d = |x₂-x₁| + |y₂-y₁|

Use when:
- Grid-like movement
- City blocks
- Robot navigation
- Less sensitive to outliers

Example:

A(2,3)

B(5,7)

Distance = |5-2| + |7-3|

= 3 + 4

= 7

---

# Euclidean vs Manhattan

| Euclidean                 | Manhattan |
|---------------------------|-----------|
| Straight-line distance    | Grid distance |
| Allows diagonal movement  | No diagonal movement |
| Most commonly used        | Used in grid-based problems |

---

# Why Feature Scaling?

KNN depends on distance.

If one feature has much larger values than another, it dominates the distance calculation.

Example:

Age: 20–60

Salary: 20,000–500,000

Without scaling, Salary has much more influence than Age.

Use:
- StandardScaler
- MinMaxScaler

before applying KNN.

---

# Choosing K

Small K (e.g., 1)
- Can overfit
- Sensitive to noise

Large K (e.g., 100)
- Can underfit
- Smoother predictions

A common starting point is **K = 5**.

---

# Advantages

- Simple
- Easy to understand
- Works for Classification & Regression
- No training phase

---

# Disadvantages

- Slow on large datasets
- Needs feature scaling
- Sensitive to irrelevant features
- Suffers from the Curse of Dimensionality

---

# Quick Summary

KNN is simple, requires no training, works for both classification and regression,
makes no assumptions about the data, and can model complex patterns by using the nearest neighbors.

- KNN predicts using the **K nearest neighbors**.
- Distance metrics determine which neighbors are closest.
- **Euclidean Distance** is used for most continuous numerical data.
- **Manhattan Distance** is useful for grid-like movement and can be more robust to outliers.
- Always scale numerical features before using KNN.
"""