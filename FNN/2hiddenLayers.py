import numpy as np

def relu(x):
    return np.maximum(0, x)

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

inputs = np.array([8, 7, 5])

# Hidden Layer 1 — 3 neurons
# 3 rows (neurons) × 3 columns (inputs)
w_hidden1 = np.array([
    [0.9, 0.1, 0.8],
    [0.5, 0.6, 0.7],
    [0.2, 0.4, 0.9],
])
b_hidden1 = np.array([0.5, 0.3, 0.1])

# Hidden Layer 2 — 2 neurons
# 2 rows (neurons) × 3 columns (hidden1 outputs)
w_hidden2 = np.array([
    [0.7, 0.3, 0.5],
    [0.2, 0.8, 0.4],
])
b_hidden2 = np.array([0.2, 0.4])

# Output Layer — 1 neuron
# 1 row × 2 columns (hidden2 outputs)
w_output = np.array([0.6, 0.5])
b_output = 0.1

# FORWARD PASS
# Hidden Layer 1
z1 = np.dot(w_hidden1, inputs) + b_hidden1
a1 = relu(z1)
print(f"Hidden1 z: {z1}")
print(f"Hidden1 a: {a1}")

# Hidden Layer 2
z2 = np.dot(w_hidden2, a1) + b_hidden2
a2 = relu(z2)
print(f"Hidden2 z: {z2}")
print(f"Hidden2 a: {a2}")

# Output Layer
z3 = np.dot(w_output, a2) + b_output
a3 = sigmoid(z3)
print(f"Output z:  {z3:.4f}")
print(f"Output a:  {a3:.4f}")

result = "PASS" if a3 > 0.5 else "FAIL"
print(f"Decision:  {result}")



















