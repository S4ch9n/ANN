import math

def tanh(x):
    return (math.exp(x) - math.exp(-x)) / \
           (math.exp(x) + math.exp(-x))

def tanh_derivative(x):
    t = tanh(x)
    return 1 - t**2        # ← the beautiful formula!

test_values = [-2, -1, 0, 1, 2]
print(f"{'x':<6} {'tanh':<12} {'derivative'}")
print("-" * 32)
for x in test_values:
    t  = tanh(x)
    td = tanh_derivative(x)
    print(f"{x:<6} {t:<12.4f} {td:.4f}")