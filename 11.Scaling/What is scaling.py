"""
Scaling is a technique used in machine learning to standardize the range of independent variables 
or features of data. 
It is a crucial step in the preprocessing phase of machine learning algorithms, 
especially those that are sensitive to the scale of data, such as gradient descent-based algorithms.
There are several common methods of scaling:

1. Min-Max Scaling (Normalization): This method scales the data to a fixed range, usually [0, 1]. 
   The formula is: X_scaled = (X - X_min) / (X_max - X_min)

2. Standardization (Z-score Scaling): This method scales the data 
   to have a mean of 0 and a standard deviation of 1.
   The formula is: X_scaled = (X - mean) / standard_deviation

3. Robust Scaling: This method is similar to standardization 
   but uses the median and interquartile range instead of mean and standard deviation.
    The formula is: X_scaled = (X - median) / IQR

Scaling is important because it can improve the performance of machine learning algorithms.
It prevents bias towards features with larger ranges and helps algorithms converge faster.
K nearest neighbors, support vector machines, and neural networks 
are examples of algorithms that can benefit from scaling.


Scaler Selection Guide
Situation-	                                                Best Choice-

No outliers	                                                Min-Max Scaler

Normal distribution	                                      Standard Scaler

Many outliers	                                            Robust Scaler

Neural Networks	                                         Min-Max Scaler

Linear Regression, Logistic Regression, SVM	             Standard Scaler

Data with extreme values	                                Robust Scaler

"""