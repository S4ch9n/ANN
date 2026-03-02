# WITHOUT activation function
# Let's stack 3 layers and see what happens

def neuron(inputs, weights, bias):
    return sum(x * w for x, w in zip(inputs, weights)) + bias

# Same input going through 3 layers
input_data = [2, 3]

# Layer 1
w1 = [0.5, 0.8]
b1 = 1
layer1_output = neuron(input_data, w1, b1)
print(f"Layer 1 output: {layer1_output}")

# Layer 2 (takes layer1 output as input)
w2 = [0.6, 0.4]
b2 = 0.5
layer2_output = neuron([layer1_output, layer1_output], w2, b2)
print(f"Layer 2 output: {layer2_output}")

# Layer 3 (takes layer2 output as input)
w3 = [0.3, 0.7]
b3 = 0.2
layer3_output = neuron([layer2_output, layer2_output], w3, b3)
print(f"Layer 3 output: {layer3_output}")

print(f"\nFinal output: {layer3_output}")
print("Is this just simple math? YES — straight line all the way through")

# ```
# Layer 1 output: 4.3
# Layer 2 output: 4.77       ← just scaled version of layer 1
# Layer 3 output: 4.962      ← just scaled version of layer 2

# All 3 layers = still just one straight line calculation
# 3 layers was POINTLESS without activation



# WITH activation — ReLU (block all negatives)
def relu(x):
    return max(0, x)           # if negative → 0, if positive → keep it

# Test it manually first
print("=== ReLU behaviour ===")
print(relu(-10))    # → 0
print(relu(-1))     # → 0
print(relu(0))      # → 0
print(relu(1))      # → 1
print(relu(10))     # → 10

print()

# WITH activation — Sigmoid (squish between 0 and 1)
import math
def sigmoid(x):
    return 1 / (1 + math.exp(-x))    # always outputs 0 to 1

print("=== Sigmoid behaviour ===")
print(sigmoid(-10))   # → nearly 0
print(sigmoid(-1))    # → 0.27
print(sigmoid(0))     # → exactly 0.5
print(sigmoid(1))     # → 0.73
print(sigmoid(10))    # → nearly 1