import numpy as np

# Activation functions
def relu(x):
    return np.maximum(0, x)

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

# Network weights
w_hidden = np.array([
    [0.9, 0.1, 0.8],
    [0.5, 0.6, 0.7],
    [0.2, 0.4, 0.9],
])
b_hidden = np.array([0.5, 0.3, 0.1])
w_output = np.array([0.6, 0.5, 0.7])
b_output = 0.1

def forward_pass(inputs):
    print(f"\nInput: {inputs}")
    print("─" * 35)

    # Hidden layer
    z_hidden = np.dot(w_hidden, inputs) + b_hidden
    a_hidden = relu(z_hidden)
    print(f"Hidden raw (z):    {z_hidden}")
    print(f"Hidden ReLU (a):   {a_hidden}")

    # Output layer
    z_output = np.dot(w_output, a_hidden) + b_output
    a_output = sigmoid(z_output)
    print(f"Output raw (z):    {z_output:.4f}")
    print(f"Output sigmoid(a): {a_output:.4f}")

    result = "PASS" if a_output > 0.5 else "FAIL"
    print(f"Decision:          {result}")
    return a_output

# Test students
strong = np.array([8, 7, 5])
weak   = np.array([1, 2, 0])

forward_pass(strong)
forward_pass(weak)