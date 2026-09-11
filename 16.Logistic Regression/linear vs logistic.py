"""
Linear Regression vs Logistic Regression

1. Purpose
- Linear Regression: Used to predict continuous numerical values.
  Example: House price, salary, temperature.

- Logistic Regression: Used to predict categories/classes.
  Example: Spam/Not Spam, Pass/Fail, Disease/No Disease.

2. Output
- Linear Regression outputs any real number.
  Example: 45000, 72.5, 120000

- Logistic Regression outputs a probability between 0 and 1.
  Example: 0.85 (85% chance of passing)

3. Formula
Linear Regression:
y = wx + b

Logistic Regression:
p = 1 / (1 + e^-(wx + b))

4. Output Range
- Linear Regression: (-∞, +∞)
- Logistic Regression: (0, 1)

5. Cost Function
- Linear Regression: Mean Squared Error (MSE)
- Logistic Regression: Log Loss (Cross Entropy Loss)

6. Problem Type
- Linear Regression: Regression Problems
- Logistic Regression: Classification Problems

Example of Linear Regression
Experience (Years): 1, 3, 5
Salary (k$): 15, 35, 55

Learned equation:
Salary = 10 × Experience + 5

For 4 years of experience:
Salary = 10 × 4 + 5 = 45

Output: 45 (continuous value)

Example of Logistic Regression
Study Hours: 1, 3, 5, 7
Pass: No, No, Yes, Yes

Model prediction:
P(Pass) = 0.85

Since 0.85 > 0.5,
Prediction = Pass (1)

Output: Probability and Class Label

Why Logistic Regression Uses Sigmoid?
Linear Regression can produce values like:
-5, 20, 100

These cannot represent probabilities.

Sigmoid Function:
σ(z) = 1 / (1 + e^(-z))

It converts any value into a range between 0 and 1.

Which One Is Better?
Neither is better overall.

Use Linear Regression when you need to predict a numerical value.

Use Logistic Regression when you need to classify data into categories.

Simple Rule:
- Linear Regression → "How much?"
- Logistic Regression → "Which class?"

Summary:
Linear Regression predicts continuous values.
Logistic Regression predicts probabilities and classes.
Choose the model based on the problem type.

"""
