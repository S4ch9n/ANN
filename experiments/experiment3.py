import numpy as np

# training data (AND gate)
X = np.array([
    [0, 0],
    [0, 1],
    [1, 0],
    [1, 1]
])

y = np.array([0, 0, 0, 1])

# initialize weights and bias
w = np.zeros(2)
b = 0

lr = 0.1   # learning rate

# training loop
for epoch in range(10): #Train the model 10 times over the dataset
      #Each full pass through the data is called an epoch.
    for i in range(len(X)):
        z = np.dot(X[i], w) + b
        y_pred = 1 if z >= 0 else 0
        
        error = y[i] - y_pred
        
        w += lr * error * X[i]
        b += lr * error

print("Weights:", w)
print("Bias:", b)