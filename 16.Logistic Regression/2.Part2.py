import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_theme()


# Define features: column 0 is Age, column 1 is Ticket Price
X = np.array([
    [10 , 3 ],
    [20 , 5 ],
    [35, 20],
    [50, 10],
])

# Define target labels: 0 (did not survive), 1 (survived)
y = np.array([0, 0, 1, 1])



def make_prediction(X, W, b, threshold=0.5):
  """
  Calculates the model output for each example in X.
  """
  m = X.shape[0]
  prob_list = np.zeros((m,))

  for i in range(m):
    # Calculate z = w1*x1 + w2*x2 + ... + b
    z = np.dot(W, X[i]) + b
    # Convert z into a probability
    prob_list[i] = sigmoid(z)

  # If probability > threshold, return True (1), else False (0)
  prediction = (prob_list > threshold)
  return prediction

def sigmoid(z):
    return 1 / (1+ np.exp(-z))     

def compute_cost(X, y, W, b):
  """
  Computes the Binary Cross-Entropy Cost.
  """
  m = X.shape[0]
  total_cost = 0.0

  for i in range(m):
    z = np.dot(W, X[i]) + b
    prob = sigmoid(z)
    # Log Loss formula: -[y*log(p) + (1-y)*log(1-p)]
    # We sum the inner part here and negate later
    total_cost += (y[i] * np.log(prob)) + ((1 - y[i]) * np.log(1 - prob))

  # Average the cost and negate
  return total_cost / (-m)

def calculate_gradient(X, y, W, b):
  """
  Computes the partial derivatives of the cost w.r.t parameters.
  """
  m, n = X.shape
  dj_dw = np.zeros((n,))
  dj_db = 0.0

  for i in range(m):
    z = np.dot(W, X[i]) + b
    prob = sigmoid(z)
    # Difference between prediction and actual label
    error = prob - y[i]

    # Gradient for bias
    dj_db += error

    # Gradient for each weight
    for j in range(n):
      dj_dw[j] += error * X[i, j]

  # Return average gradients
  return dj_dw / m, dj_db / m

def gradient_descent(X, y, w_input, b_input, max_iter, alpha=0.01):
  """
  Optimizes W and b by moving in the direction of steepest descent.
  """
  w = w_input
  b = b_input
  cost_history = []

  for i in range(max_iter):
    # Step 1: Compute gradients
    dj_dw, dj_db = calculate_gradient(X, y, w, b)

    # Step 2: Update parameters (w = w - learning_rate * gradient)
    w = w - alpha * dj_dw
    b = b - alpha * dj_db

    # Step 3: Record the cost to monitor convergence
    if i % 100 == 0:
      cost = compute_cost(X, y, w, b)
      cost_history.append(cost)
      

  return w, b, cost_history

n = X.shape[1] #number of features
w_init = np.zeros((n,)) # Initialize weights to zeros
b_init = 0.0


w_final, b_final, cost_history = gradient_descent(X, y, w_input=w_init, b_input=b_init, max_iter=100000, alpha=0.01)
print("Final Weights (W):", w_final)
print("Final Bias (b):", b_final)

prediction = make_prediction(X, w_final, b_final).astype(int)

print("Final Model Predictions:", prediction)
print("Actual Target Labels:   ", y)