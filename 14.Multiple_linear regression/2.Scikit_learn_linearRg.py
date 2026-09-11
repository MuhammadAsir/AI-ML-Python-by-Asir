import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import SGDRegressor
"""
from sklearn.linear_model import LinearRegression:
we are importing the LinearRegression class from the linear_model module of the scikit-learn library. 
This class is used to perform linear regression, 
which is a statistical method for modeling the relationship between a dependent variable and one or more independent variables.


from sklearn.linear_model import SGDRegressor: 
we are importing the SGDRegressor class from the linear_model module of the scikit-learn library.
This class is used to perform linear regression using Stochastic Gradient Descent (SGD) optimization,
which is an iterative method for optimizing the cost function of a linear regression model.

"""
x = np.array([
    [1,4, 1.5, 3.8],
    [3,6, 1.0, 3.1],
    [4,7, 0.8, 3.9],
    [5,8, 0.4, 3.4],
    [7,9, 0.2, 2.8]
])

y = np.array([45.9 ,  76.55,  92.35, 107.9 , 128. ])
model1=LinearRegression()
model1.fit(x,y)

weights=model1.coef_ #It means the coefficients (weights) of the linear regression model that has been fitted to the data.
bias=model1.intercept_ #It means the intercept (bias) of the linear regression model that has been fitted to the data.
print(weights)
print(bias)


model2 = SGDRegressor(penalty=None,max_iter=10000000,learning_rate="constant")
#penalty=None means that we are not applying any regularization to the model

model2.fit(x,y)


weights= model2.coef_
bias = model2.intercept_

print(weights)
print(bias)


"""
The SGDRegressor implements Stochastic Gradient Descent.
It's particularly useful for very large datasets where the standard LinearRegression 
might be too slow.

Before we used standard batch gradient descent to optimize the weights and bias, 
which calculates the cost function and updates the parameters based on the entire dataset.

In contrast, Stochastic Gradient Descent (SGD) updates the parameters based on a single example 
at a time, which can lead to faster convergence, especially for large datasets.

So SGDRegressor use single example at a time to update the weights and bias, 
which can be more efficient for large datasets compared to batch gradient descent
used in LinearRegression.
"""