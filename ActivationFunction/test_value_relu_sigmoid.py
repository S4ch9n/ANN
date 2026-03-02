import math

def relu(x):
    return max(0, x)

def sigmoid(x):
    return 1 / (1 + math.exp(-x))

# Test both with same raw values
test_values = [-10, -5, -1, 0, 1, 5, 10]

print(f"{'Input':<8} {'ReLU':<10} {'Sigmoid'}")
print("-" * 30)
for val in test_values:
    print(f"{val:<8} {relu(val):<10} {sigmoid(val):.4f}")