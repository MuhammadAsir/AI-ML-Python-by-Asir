"""
# Random Forest, Overfitting & Underfitting

1. What is Random Forest?

Random Forest is a supervised machine learning algorithm used for:

- Classification
- Regression

It is called "Random Forest" because it combines many Decision Trees to make one final prediction.

Instead of relying on a single Decision Tree, Random Forest creates multiple trees and combines their predictions.

The idea is:

"Many weak learners together make a stronger learner."

2. Why Do We Need Random Forest?
------------------------------------------------------------

A single Decision Tree has a major problem:

- It can easily overfit the training data.
- A small change in data can produce a completely different tree.

Random Forest solves this problem by averaging the predictions of many trees.

As a result:
- Better accuracy
- Better generalization
- Less overfitting
- More stable predictions

3. How Does Random Forest Work?
------------------------------------------------------------

Step 1:
Randomly select samples from the training dataset (Bootstrap Sampling).
↓
Step 2:
Create a Decision Tree using the selected samples.
↓
Step 3:
At every split, randomly choose only a subset of features instead of using all features.
↓
Step 4:
Repeat the process to build many Decision Trees.
↓
Step 5:
Combine the predictions.

For Classification:
Majority Voting

Example:

Tree 1 -> Yes
Tree 2 -> Yes
Tree 3 -> No
Tree 4 -> Yes
Tree 5 -> No

Final Prediction = Yes

For Regression:

Take the average prediction.

Example:

Tree Predictions:

80
85
90
95

Final Prediction

= (80 + 85 + 90 + 95) / 4
= 87.5

4. Why is it Called "Random" Forest?
------------------------------------------------------------

Randomness comes from two places:

1. Randomly selecting training samples
   (Bootstrap Sampling)

2. Randomly selecting features
   at each split.

This randomness makes each tree different.

5. Advantages of Random Forest
------------------------------------------------------------

✓ High accuracy

✓ Reduces overfitting

✓ Works well on large datasets

✓ Handles missing values

✓ Handles categorical and numerical data

✓ Less sensitive to noise

✓ Can estimate feature importance

6. Disadvantages of Random Forest
------------------------------------------------------------

✗ Slower than a single Decision Tree

✗ Uses more memory

✗ Harder to interpret

✗ Large models take more time to train


7. Decision Tree vs Random Forest
------------------------------------------------------------

Decision Tree

- Single tree
- Faster
- Easy to understand
- More prone to overfitting
- Lower accuracy (sometimes)

Random Forest

- Many trees
- Slightly slower
- Hard to interpret
- Less overfitting
- Usually higher accuracy


8. What is Overfitting?
------------------------------------------------------------

Overfitting happens when a model learns the training data too well.

It learns:
- Patterns
- Noise
- Outliers

As a result:

Training Accuracy  -> Very High

Testing Accuracy   -> Low

The model memorizes the training data instead of learning general patterns.

Example:

Training Accuracy = 99%

Testing Accuracy = 80%

This is Overfitting.


Characteristics of Overfitting
------------------------------------------------------------

✓ Very high training accuracy

✓ Low testing accuracy

✓ Poor performance on unseen data

✓ High variance


Causes of Overfitting
------------------------------------------------------------

- Very deep Decision Tree
- Too many features
- Small training dataset
- Too many training iterations
- Model is too complex

------------------------------------------------------------

How to Reduce Overfitting?
------------------------------------------------------------

✓ More training data

✓ Cross-validation

✓ Feature selection

✓ Pruning Decision Trees

✓ Regularization

✓ Random Forest

✓ Early stopping (for iterative models)


9. What is Underfitting?
------------------------------------------------------------

Underfitting happens when the model is too simple to learn the data.

It cannot capture the relationship between input and output.

As a result:

Training Accuracy -> Low

Testing Accuracy -> Low

Example:

Training Accuracy = 65%

Testing Accuracy = 62%

The model performs poorly everywhere.

------------------------------------------------------------

Characteristics of Underfitting
------------------------------------------------------------

✓ Low training accuracy

✓ Low testing accuracy

✓ Poor predictions

✓ High bias

------------------------------------------------------------

Causes of Underfitting
------------------------------------------------------------

- Model is too simple
- Very few features
- Insufficient training
- Excessive regularization

------------------------------------------------------------

How to Reduce Underfitting?
------------------------------------------------------------

✓ Increase model complexity

✓ Add more useful features

✓ Train for longer (if applicable)

✓ Reduce regularization

✓ Use a more powerful algorithm

------------------------------------------------------------

10. Overfitting vs Underfitting
------------------------------------------------------------

                     Overfitting             Underfitting

Training Accuracy    Very High               Low

Testing Accuracy     Low                     Low

Learns Noise         Yes                     No

Model Complexity     Very High               Very Low

Bias                 Low                     High

Variance             High                    Low

Generalization       Poor                    Poor

------------------------------------------------------------

11. Easy Way to Remember
------------------------------------------------------------

Underfitting
-------------
"The model is too simple."

Training Accuracy = Low
Testing Accuracy = Low

------------------------------------------------------------

Good Fit
---------
"The model learns the important patterns."

Training Accuracy = High
Testing Accuracy = High

------------------------------------------------------------

Overfitting
-----------
"The model memorizes the training data."

Training Accuracy = Very High
Testing Accuracy = Low

------------------------------------------------------------

12. Interview Summary
------------------------------------------------------------

Random Forest:
An ensemble learning algorithm that builds multiple Decision Trees using random samples and random features, then combines their predictions using majority voting (classification) or averaging (regression).

Overfitting:
The model learns the training data too well, including noise, resulting in high training accuracy but poor testing accuracy.

Underfitting:
The model is too simple to learn the underlying patterns, resulting in poor performance on both training and testing data.

"""