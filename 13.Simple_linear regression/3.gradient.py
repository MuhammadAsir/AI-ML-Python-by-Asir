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

#formula: dj_dw = (1/m) * sum((pred - Y[i]) * X[i]),  dj_db = (1/m) * sum(pred - Y[i])
def cal_gradient(X,Y,w,b):
    m=X.shape[0]
    dj_dw=0.0
    dj_db=0.0
    for i in range(m):
        pred=w*X[i]+b
        error=pred-Y[i]
        dj_dw=dj_dw+error*X[i]
        dj_db=dj_db+error   

    return dj_dw/m, dj_db/m


def gradient_descent(X,Y,w_in,b_in,num_iter,alpha):
#We use num_iters iterations to update w and b. In each iteration, we calculate the gradient and update w and b using the learning rate alpha.
    w=w_in
    b=b_in
    cost_memo=[] # To store the cost at each iteration for plotting
    iteration = [] # To store the iteration numbers for plotting
    for i in range(num_iter):
        dj_dw,dj_db=cal_gradient(X,Y,w,b)
        w = w - alpha * dj_dw
        b = b - alpha * dj_db
        cost=compute_cost(X,Y,w,b)
        cost_memo.append(cost)
        iteration.append(i)# Store the cost and iteration number for plotting
        print(f"Iteration {i+1:4d} | Cost: {cost:.6f} | w: {w:.4f} | b: {b:.4f}")
        
    return w, b,cost_memo, iteration


w_final, b_final, cost_memo, iter_list = gradient_descent(X, Y, w_in=0, b_in=0, num_iter=1000, alpha=0.01)

print(f"Final parameters: w={w_final:0.4f}, b={b_final:0.4f}")

final_preds = make_prediction(X, Y, w=w_final, b=b_final)
sns.scatterplot(x=X, y=Y, color='blue', label='Data points')
plt.plot(X, final_preds, color='red', label='Best fit line')
plt.title(f"Final Cost: {compute_cost(X, Y, w_final, b_final):0.4e}")
plt.legend()
plt.show()


x_new=2 #experience 2 years

prediction= w_final*x_new+b_final
print(f"Predicted salary for {x_new} years of experience: ${prediction:0.2f}k")


#Iteration plot vs Cost

plt.plot(iter_list[:20], cost_memo[:20])
plt.xlabel("Number of Iterations")
plt.ylabel("Cost")
plt.title("Learning Curve (Cost Reduction)")
plt.show()