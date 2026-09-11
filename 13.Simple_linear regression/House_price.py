import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("Housing.csv")

x_original = np.array(df['area'])
y = np.array(df['price'])
sns.kdeplot(x=x_original,y=y,fill=True)

# Feature Scaling
x = (x_original - np.mean(x_original)) / np.std(x_original)
# Standardize the feature to have mean 0 and standard deviation.Now x is the standardized version of x_original, which can help improve the performance of gradient descent.

def make_prediction(x, w, b):
    m = x.shape[0]
    pred_list = np.zeros(m)

    for i in range(m):
        pred_list[i] = w * x[i] + b

    return pred_list


def cost_function(x, y, w, b):
    m = x.shape[0]
    cost = 0.0

    for i in range(m):
        pred = w * x[i] + b
        error = pred - y[i]
        cost += error ** 2

    return cost / (2 * m)

def gradient(x, y, w, b):
    m = x.shape[0]

    dj_dw = 0.0
    dj_db = 0.0

    for i in range(m):
        pred = w * x[i] + b
        error = pred - y[i]

        dj_dw += error * x[i]
        dj_db += error

    return dj_dw / m, dj_db / m


def gradient_descent(x, y, w_in, b_in, num_iter, alpha):

    w = w_in
    b = b_in

    cost_history = []
    iteration_history = []

    for i in range(num_iter):

        dj_dw, dj_db = gradient(x, y, w, b)

        w = w - alpha * dj_dw
        b = b - alpha * dj_db

        cost = cost_function(x, y, w, b)

        cost_history.append(cost)
        iteration_history.append(i)

        

    return w, b, cost_history, iteration_history

w_final, b_final, cost_history, iteration_history=gradient_descent(x,y,w_in=0,b_in=0,num_iter=1000,alpha=0.01)


print("Final Slope (w):", w_final)
print("Final Intercept (b):", b_final)

final_cost = cost_function(x, y, w_final, b_final)
print("Final Cost:", final_cost)

predictions = make_prediction(x, w_final, b_final)


# 11. Plot: Iteration vs Cost
plt.figure(figsize=(8,5))
plt.plot(iteration_history, cost_history)
plt.xlabel("Iteration")
plt.ylabel("Cost")
plt.title("Iteration vs Cost")
plt.grid(True)
plt.show()

# 12. Plot: Actual vs Predicted

sorted_indices = np.argsort(x_original)
"""
we didn't sort x_original itself, but we got the indices that would sort it. 
This allows us to plot the predicted line in the correct order of area values on the x-axis,
ensuring that the predicted line is plotted correctly against the actual area values.
Get the indices that would sort x_original. This is necessary to plot the predicted line 
in the correct order of area values.
"""
plt.figure(figsize=(8,5))

sns.scatterplot(x=x_original,y=y,color='blue',label='Actual Values')

plt.plot(x_original[sorted_indices],predictions[sorted_indices],color='red',linewidth=2,label='Predicted Line')
#x_original[sorted_indices] → the house areas (x-axis)
#predictions[sorted_indices] → the prices predicted by your model (y-axis)

plt.xlabel("Area")
plt.ylabel("Price")
plt.title("Actual vs Predicted Values")
plt.legend()
plt.show()