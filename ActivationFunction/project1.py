#Real task: Predict if a student will PASS or FAIL based on study hours, sleep hours, practice tests.
import math

def relu(x):
    return max(0, x)

def sigmoid(x):
    return 1 / (1 + math.exp(-x))

def neuron(i, w, b, activation):
    raw = sum(x * w for x, w in zip(i, w)) + b
    return activation(raw)

def layer(inputs, all_weights, all_biases, activation):
    outputs = []
    for w, b in zip(all_weights, all_biases):
        out = neuron(inputs, w, b, activation)  # ONE neuron at a time
        outputs.append(out)
    return outputs

def neural_network(inputs):
    
    #hidden layer (use relu)
    hidden_output = layer(inputs, all_weights, all_biases, relu)

    output_weights = [0.6, 0.5, 0.7]   # one weight per hidden neuron
    output_bias    = 0.1
    
    final = neuron(hidden_output,output_weights,output_bias,sigmoid)   
    return final



strong_student = [8, 7, 5]
weak_student   = [1, 2, 0]
all_weights = [
    [0.9, 0.1, 0.8],
    [0.5, 0.6, 0.7],
    [0.2, 0.4, 0.9],
]
all_biases = [0.5, 0.3, 0.1]

strong_result = neural_network(strong_student)

weak_result   = neural_network(weak_student)

print(f"Strong student: {strong_result:.4f}")
print(f"Weak student:   {weak_result:.4f}")

# Final decision
if strong_result > 0.5:
    print("Strong → PASS")
if weak_result < 0.5:
    print("Weak → FAIL")