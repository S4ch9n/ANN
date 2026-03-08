import math

def sigmoid(x):
    return 1 / (1 + math.exp(-x))

def sigmoid_derivative(x):
    s = sigmoid(x)
    return s * (1 - s)      # ← the beautiful formula!

# Test
test_values = [-2, -1, 0, 1, 2]
print(f"{'x':<6} {'sigmoid':<12} {'derivative'}")
print("-" * 32)
for x in test_values:
    s  = sigmoid(x)
    sd = sigmoid_derivative(x)
    print(f"{x:<6} {s:<12.4f} {sd:.4f}")