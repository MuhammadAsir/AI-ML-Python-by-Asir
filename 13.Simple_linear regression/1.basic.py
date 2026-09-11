import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

X = np.array([1 , 3, 4, 6, 7]) # Input feature: years of experience
Y = np.array([15,35,45,65,75]) # Target value: salary (in thousands)
# Set default styles for our plots
sns.set_theme()


def make_prediction(X, Y, w, b):
  """Calculates the model output: f(x) = wx + b"""
  m = X.shape[0] # Number of training examples
  pred_list = np.zeros((m,)) # Initialize an array to store results

  for i in range(m):
    # Apply the linear regression formula
    pred_list[i] = w * X[i] + b

  return pred_list

def compute_cost(X, Y, w, b):
    m = X.shape[0]
    cost = 0.0

    for i in range(m):
        pred = w * X[i] + b
        error = pred - Y[i]
        error_squared = error ** 2
        cost = cost + error_squared

    cost = cost / (2 * m)
    return cost

w = 10.0
b = 5.0
predictions = make_prediction(X, Y, w=w, b=b)
print(predictions)
cost=compute_cost(X, Y, w=w, b=b)
sns.scatterplot(x=X, y=Y)
plt.plot(X, predictions)
# The title shows the cost, helping us see how 'wrong' our line is
plt.title(f"Cost: {cost}, for w={w} and b={b}")
plt.show()
