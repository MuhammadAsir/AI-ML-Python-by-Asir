import numpy as np

# dataset: [study_hours, playtime_hours, marks]
data = np.array([
    [2, 5, 45],
    [3, 4, 50],
    [4, 4, 55],
    [5, 3, 65],
    [6, 3, 70],
    [7, 2, 78],
    [8, 2, 85],
    [1, 6, 40],
    [9, 1, 92],
    [10, 1, 96]
])

random_index=np.random.choice(10,size=(10,),replace=False)
print(random_index)

data=data[random_index]
print(data)


x=data[: , :2]  #feature, study_hours, playtime

y=data[: , 2:] #target, marks


# train-test split (80-20)
train_index=int(len(data)*0.8) 
x_train=x[:train_index,:]
y_train=y[:train_index,:]

print("X train",x_train,'\n')
print("Y train",y_train,'\n')

x_test=x[train_index:,:]
y_test=y[train_index:,:]

print("X test",x_test,'\n')
print("Y test",y_test,'\n')





