import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_theme()
x = np.array([
    [1,4, 1.5, 3.8],
    [3,6, 1.0, 3.1],
    [4,7, 0.8, 3.9],
    [5,8, 0.4, 3.4],
    [7,9, 0.2, 2.8]
])

y = np.array([45.9 ,  76.55,  92.35, 107.9 , 128. ])

sns.scatterplot(x=x[:,0:1].ravel(), y=y) #used ravel() to convert 2D array to 1D array
plt.xlabel("Years of Experience")
plt.ylabel("Salary")



def make_pred(x,w,b):
    m=x.shape[0]
    pred_list=np.zeros((m,))

    for i in range(m):
        pred_list[i]=np.dot(w,x[i])+b #use dot product for multiple features

    return pred_list


def compute_cost(x, y, w, b):
  """Calculates the Mean Squared Error (MSE) to measure model accuracy"""
  m = x.shape[0]
  cost = 0.0

  pred_list = make_pred(x,w,b) # we didn't use for loop here because we already have a function that can make predictions for all examples at once
  error = pred_list - y
  error_squared = error ** 2
  cost = np.sum(error_squared) #Used np.sum() instead of cost += error_squared[i] because we can calculate the cost for all examples at once using vectorized operations
  cost = cost / (2 * m)

  return cost

m=x.shape[0]
n=x.shape[1]#number of features
w_init=np.ones((n,)) #initialize weights for all features
b_init=1.0

prediction=make_pred(x,w_init,b_init)
print("Predictions with initial weights and bias:", prediction)

def calculate_gradient(x, y, w, b):
  
  m = x.shape[0]
  n = x.shape[1]

  dj_dw = np.zeros((n,)) ## jotota feature totota weights
  dj_db = 0.0 # Change needed for bias

  for i in range(m):
    prediction = np.dot(w,x[i]) + b
    error = prediction - y[i]
    dj_db = dj_db +  error # Update bias gradient
    
    for j in range(n):
      dj_dw[j] = dj_dw[j] + (error * x[i,j])



  return dj_dw / m, dj_db / m

print("Gradient with initial weights and bias:", calculate_gradient(x, y, w_init, b_init))


def gradient_descent(x, y, w_input, b_input, max_iter, alpha=0.01):
  """Automates the tuning of w and b to minimize cost"""
  w = w_input
  b = b_input
  cost_memo = []
  iteration = []

  for i in range(max_iter):
    # 1. Calculate the gradients (the slope)
    dj_dw, dj_db = calculate_gradient(x, y, w, b)

    # 2. Update parameters by taking a small step (alpha) against the gradient

    w = w - alpha * dj_dw
    b = b - alpha * dj_db

    # 3. Track progress by saving the cost
    cost = compute_cost(x,y, w, b)
    cost_memo.append(cost)
    iteration.append(i)

    
  return w, b, cost_memo, iteration

w_final, b_final, cost_memo, iter_list = gradient_descent(x, y, w_input=w_init, b_input=b_init, max_iter=100000, alpha=0.01)

print("Final weights:", w_final)#print the final weights for all features
print("Final bias:", b_final)#print the final bias

X_test=  [2,10, 1.5, 3.8]

prediction_of_new_data = w_final[0] * X_test[0] +w_final[1] * X_test[1] + w_final[2] * X_test[2] + w_final[3] * X_test[3] + b_final

print(prediction_of_new_data)