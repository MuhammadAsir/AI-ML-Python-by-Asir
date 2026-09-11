"""
Cross-validation is a technique in Machine Learning used to evaluate 
how well a model will perform on unseen data.
Instead of training and testing a model only once, 
cross-validation repeatedly splits the dataset into different training 
and testing parts to get a more reliable estimate of model performance.

=========================
5-Fold Cross Validation
=========================

Suppose we have 10 samples.

S1 S2 S3 S4 S5 S6 S7 S8 S9 S10

We choose:

k = 5

Since there are 10 samples,

10 / 5 = 2

Each fold contains 2 samples.

----------------------------------------
Step 1: Split the dataset
----------------------------------------

Fold 1 = S1 S2
Fold 2 = S3 S4
Fold 3 = S5 S6
Fold 4 = S7 S8
Fold 5 = S9 S10

----------------------------------------
Iteration 1
----------------------------------------

Training Data:
S3 S4 S5 S6 S7 S8 S9 S10

Testing Data:
S1 S2

Accuracy = 90%

----------------------------------------
Iteration 2
----------------------------------------

Training Data:
S1 S2 S5 S6 S7 S8 S9 S10

Testing Data:
S3 S4

Accuracy = 92%

----------------------------------------
Iteration 3
----------------------------------------

Training Data:
S1 S2 S3 S4 S7 S8 S9 S10

Testing Data:
S5 S6

Accuracy = 88%

----------------------------------------
Iteration 4
----------------------------------------

Training Data:
S1 S2 S3 S4 S5 S6 S9 S10

Testing Data:
S7 S8

Accuracy = 91%

----------------------------------------
Iteration 5
----------------------------------------

Training Data:
S1 S2 S3 S4 S5 S6 S7 S8

Testing Data:
S9 S10

Accuracy = 89%

----------------------------------------
Final Result
----------------------------------------

Fold 1 = 90%
Fold 2 = 92%
Fold 3 = 88%
Fold 4 = 91%
Fold 5 = 89%

Average Accuracy

= (90 + 92 + 88 + 91 + 89) / 5
= 450 / 5
= 90%

----------------------------------------
Important Points
----------------------------------------

1. The dataset is divided into k equal folds.

2. In each iteration:
   - One fold is used for testing.
   - The remaining folds are used for training.

3. Every sample is used:
   - Once as testing data.
   - (k - 1) times as training data.

4. The model is trained from scratch in every iteration.

5. The final performance is the average of all k test scores.

----------------------------------------
Why Use Cross Validation?
----------------------------------------

✔ Gives a more reliable estimate of model performance.

✔ Reduces the effect of a lucky or unlucky train-test split.

✔ Helps detect overfitting.

✔ Makes better use of small datasets.

✔ Commonly used for model selection and hyperparameter tuning.

"""