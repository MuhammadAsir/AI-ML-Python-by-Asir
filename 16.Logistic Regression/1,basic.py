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

def sigmoid(z):
    return 1 / (1+ np.exp(-z))     

z = np.arange(-10, 11, 0.1)#arrange of values from -10 to 10 with a step of 0.1
sigmoid_values = sigmoid(z)
# Plot the sigmoid function
plt.plot(z, sigmoid_values)
plt.title("Sigmoid Activation Function")
plt.xlabel("Z (Linear Combination)")
plt.ylabel("Probability")
plt.grid(True)
plt.show()