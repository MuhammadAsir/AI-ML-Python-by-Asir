"""
Decision Tree - Quick Notes


1. What is a Decision Tree?

A Decision Tree is a supervised machine learning algorithm used for:
- Classification
- Regression

It learns by asking a series of questions (splits) on the features to separate the data into smaller and purer groups.
Example:

                Age > 30?
               /        \
             Yes        No
            /             \
      Income > 50K?      Student?
        /      \          /     \
      Buy    Don't      Buy    Don't

2. Goal of a Decision Tree
--------------------------
The goal is to find the BEST feature to split the dataset.

Decision Trees use impurity measures such as:
1. Entropy
2. Information Gain (IG)
3. Gini Index

-----------------------
3. Entropy

Entropy measures how mixed or impure the data is.

Formula:
Entropy(S) = -Σ (pi × log2(pi))

where:
pi = probability of each class

Example 1:

Yes = 50
No  = 50

Entropy = 1
Maximum uncertainty (completely mixed).

Example 2:

Yes = 100
No  = 0

Entropy = 0

Perfectly pure.

Interpretation:

More mixed  -> Higher Entropy
More pure   -> Lower Entropy

Range (Binary Classification):

0 -------------------- 1
Pure                Maximum Impurity


------------------------------------------------------------

4. Information Gain (IG)
------------------------
Information Gain tells us how much entropy decreases after splitting.

Formula:

IG = Entropy(parent) - Weighted Entropy(children)

Decision Tree always chooses the feature with the HIGHEST Information Gain.

Higher IG means:
- Better split
- More purity
- Less uncertainty


Example:

Before split:

Entropy = 0.94

After split:

Weighted Entropy = 0.40

Information Gain:

IG = 0.94 - 0.40
IG = 0.54

Since IG is high, this split is considered good.


5. Gini Index
-------------
Gini Index is another measure of impurity.

Formula:

Gini = 1 - Σ(pi²)

For binary classification:

Gini = 1 - (p² + (1-p)²)


Example 1:

Yes = 100
No  = 0

Gini = 0

Perfectly pure.


Example 2:

Yes = 50
No  = 50

Gini = 0.5

Maximum impurity for binary classification.


Interpretation:

Lower Gini = Better split
Higher Gini = More impurity

Range (Binary Classification):

0 -------------------- 0.5
Pure              Maximum Impurity


6. Entropy vs Gini
------------------

Feature                 Entropy                 Gini
--------------------------------------------------------------
Formula                 Uses log2              No logarithm
Speed                   Slower                 Faster
Measures                Uncertainty            Impurity
Best Value              Lower                  Lower
Used By                 ID3, C4.5              CART


------------------------------------------------------------

7. Decision Tree Building Process
---------------------------------

Step 1:
Start with the entire training dataset.

↓

Step 2:
Calculate Entropy (or Gini).

↓

Step 3:
Try splitting using every feature.

↓

Step 4:
Calculate Information Gain (or Gini Reduction).

↓

Step 5:
Choose the feature with:
- Highest Information Gain
OR
- Lowest Gini

↓

Step 6:
Split the dataset.

↓

Step 7:
Repeat the same process for every child node.

↓

Step 8:
Stop when:
- The node becomes pure.
- Maximum depth is reached.
- Minimum samples condition is met.
- No further useful split is possible.


------------------------------------------------------------

8. Relationship Between All Concepts
------------------------------------

Dataset
   │
   ▼
Calculate Entropy (or Gini)
   │
   ▼
Try every feature
   │
   ▼
Calculate Information Gain
(or Gini Reduction)
   │
   ▼
Choose the Best Feature
   │
   ▼
Split the Dataset
   │
   ▼
Repeat Until Stopping Condition


------------------------------------------------------------

9. Which Algorithm Uses Which Criterion?
----------------------------------------

ID3   -> Entropy + Information Gain

C4.5  -> Gain Ratio (based on Entropy)

CART  -> Gini Index (Classification)
         MSE (Regression)


------------------------------------------------------------

10. Quick Revision
------------------

Decision Tree
-------------
A supervised learning algorithm that repeatedly splits data into smaller and purer groups.

Entropy
-------
Measures uncertainty or impurity.
Lower entropy means purer data.

Information Gain
----------------
Measures how much entropy decreases after a split.
Higher Information Gain means a better split.

Gini Index
----------
Measures impurity.
Lower Gini means a better split.

ID3 uses Entropy + Information Gain.

CART uses Gini Index.

------------------------------------------------------------

11. Easy Way to Remember
------------------------

Entropy  -> Measures "How mixed is the data?"

Information Gain -> "How much impurity did we remove?"

Gini -> "Another way to measure impurity (faster than entropy)."

Decision Tree -> "Choose the split that makes the data as pure as possible."

"""