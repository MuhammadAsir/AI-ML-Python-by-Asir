import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns



X = np.array([1 , 3, 4, 6, 7]) # Input feature: years of experience
Y = np.array([15,35,45,65,75]) # Target value: salary (in thousands)
# Set default styles for our plots
sns.set_theme()

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

w_range = [] # To store different values of w
cost_history = [] # To store the corresponding cost for each w

for i in range(-100,100):
    cost_i=compute_cost(X, Y, w=i, b=0) # Compute cost for w=i and a fixed b
    w_range.append(i) # Append the current w value to the list
    cost_history.append(cost_i) # Append the computed cost to the history list

plt.plot(w_range, cost_history) # Plot w values against their corresponding costs
plt.xlabel("weights - w")
plt.ylabel("Cost - J(w)")
plt.title("Cost Function Visualization")
plt.show()
