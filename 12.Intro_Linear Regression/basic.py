import numpy as np 
import matplotlib.pyplot as plt 
import seaborn as sns 


X = np.array([1 , 3, 4, 6, 7]) # Years of experience

Y = np.array([15, 35, 45, 65, 75]) # Salary in thousands


def make_predictions(X,Y, w, b):  #We use declare function for making predictions using the linear regression model
    m=X.shape[0]# Number of training examples
    pred = np.zeros((m,)) # Create an empty array to store our results
    for i in range(m):
        pred[i]=w*X[i]+b

    return pred


predictions=make_predictions(X,Y,10,5)
sns.scatterplot(x=X, y=Y,label='Actual Salary')
plt.plot(X, predictions, color='red', label='Model Line')
plt.show()

#practice problem link
"""
https://colab.research.google.com/drive/10cHV_oRmgA-iv86F-2owEqq2VEidwvmh

"""