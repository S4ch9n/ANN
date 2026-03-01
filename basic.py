# No libraries needed — pure Python math!

# === INPUTS (house features) ===
size     = 1500   # sq ft
rooms    = 3
location = 8      # out of 10
# === INPUTS (house features) ===
size     = 1500   # sq ft
rooms    = 3
location = 8  
# === WEIGHTS (how important each input is) ===
w_size     = 0.8
w_rooms    = 0.5
w_location = 0.9

# === BIAS ===
bias = 50

# === ONE NEURON CALCULATION ===
output = (size * w_size) + (rooms * w_rooms) + (location * w_location) + bias

print(f"Predicted House Price Score: {output}")
# Output: 1258.7




#basic neuron function
# This is the most important function in neural networks
def neuron(input, weight, bias):
    output = (input * weight) + bias
    return output

# Test it
print(neuron(5, 2, 1))   # → 11
print(neuron(0, 2, 1))   # → 1  (bias saves us from 0!)
print(neuron(5, 0, 1))   # → 1  (weight=0, input ignored)



# Multiple Inputs → One Neuron
def neuron_multi(inputs, weights, bias):
    total = 0
    for i in range(len(inputs)):
        total += inputs[i] * weights[i]   # multiply each input by its weight
    total += bias
    return total

# Test it
inputs  = [2, 3, 4]
weights = [0.5, 0.8, 0.2]
bias    = 1

print(neuron_multi(inputs, weights, bias))
# = (2×0.5) + (3×0.8) + (4×0.2) + 1
# = 1 + 2.4 + 0.8 + 1
# = 5.2


#Dot Product (Shorter Way to Write Same Thing)
# Python has a shortcut for multiply-then-sum
def dot_product(inputs, weights):
    total = 0
    for i in range(len(inputs)):
        total += inputs[i] * weights[i]
    return total

inputs  = [2, 3, 4]
weights = [0.5, 0.8, 0.2]

print(dot_product(inputs, weights))  # → 4.2

# Same thing with zip() — cleaner code
def dot_product_clean(inputs, weights):
    return sum(x * w for x, w in zip(inputs, weights))

print(dot_product_clean(inputs, weights))  # → 4.2  same result!


#Full Neuron Using Dot Product
def neuron_v2(inputs, weights, bias):
    return sum(x * w for x, w in zip(inputs, weights)) + bias

inputs  = [2, 3, 4]
weights = [0.5, 0.8, 0.2]
bias    = 1

print(neuron_v2(inputs, weights, bias))  # → 5.2


# Layer of Neurons (Multiple Neurons Together)
# This is a LAYER — multiple neurons processing same inputs
def layer(inputs, all_weights, all_biases):
    outputs = []
    for weights, bias in zip(all_weights, all_biases):
        output = neuron_v2(inputs, weights, bias)
        outputs.append(output)
    return outputs

inputs = [2, 3, 4]

# 3 neurons = 3 sets of weights, 3 biases
all_weights = [
    [0.5, 0.8, 0.2],   # neuron 1 weights
    [0.1, 0.9, 0.4],   # neuron 2 weights
    [0.7, 0.3, 0.6],   # neuron 3 weights
]
all_biases = [1, 0.5, 2]

result = layer(inputs, all_weights, all_biases)
print(result)   # → [5.2, 4.5, 8.3]  ← 3 outputs from 3 neurons



# Multiple inputs, ONE weight list = ONE neuron
inputs = [
    [2, 1, 3],
    [3, 5, 4],
    [1, 2, 6],
]
weights = [0.5, 0.8, 0.2]   # one neuron
bias    = 1

for i, sample in enumerate(inputs):
    output = sum(x * w for x, w in zip(sample, weights)) + bias
    print(f"Sample {i+1} output: {output}")

# Sample 1: (2×0.5) + (1×0.8) + (3×0.2) + 1 = 3.4
# Sample 2: (3×0.5) + (5×0.8) + (4×0.2) + 1 = 6.3
# Sample 3: (1×0.5) + (2×0.8) + (6×0.2) + 1 = 4.3
# **Each sample gets its own output from the same neuron**


# Full transparency — see every calculation
def neuron_explained(inputs, weights, bias):
    print("=== Neuron Calculation ===")
    total = 0
    for i in range(len(inputs)):
        step = inputs[i] * weights[i]
        print(f"  input[{i}] {inputs[i]} × weight[{i}] {weights[i]} = {step}")
        total += step
    print(f"  Sum = {total}")
    print(f"  + bias {bias}")
    print(f"  Output = {total + bias}")
    return total + bias

neuron_explained([2, 3, 4], [0.5, 0.8, 0.2], 1)