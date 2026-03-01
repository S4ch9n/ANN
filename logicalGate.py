import numpy as np
from sklearn.neural_network import MLPClassifier

# AND gate data
X = np.array([[0,0],[0,1],[1,0],[1,1]])
Y = np.array([0,0,0,1])

# Neural Network model
model = MLPClassifier(hidden_layer_sizes=(2,), activation='logistic', max_iter=5000)

# Train
model.fit(X, Y)

# Predict
print("Predictions:")
print(model.predict(X))