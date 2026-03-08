def relu(x):
    return max(0, x)

def relu_derivative(x):
    return 1 if x > 0 else 0    # simplest derivative ever!

test_values = [-2, -1, 0, 1, 2]
print(f"{'x':<6} {'relu':<10} {'derivative'}")
print("-" * 28)
for x in test_values:
    r  = relu(x)
    rd = relu_derivative(x)
    print(f"{x:<6} {r:<10} {rd}")