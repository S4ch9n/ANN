import numpy as np

X = np.array([[0,0],[0,1],[1,0],[1,1]])
y = np.array([0,0,0,1])

w  = np.zeros(2)
b  = 0
lr = 0.1

for epoch in range(100):
    for i in range(len(X)):
        z      = np.dot(X[i], w) + b
        y_pred = 1 if z > 0 else 0   # ← changed >= to >
        error  = y[i] - y_pred
        w     += lr * error * X[i]
        b     += lr * error

print("Final Weights:", w)
print("Final Bias:", b)

# Verify
print("\nVerification:")
for i in range(len(X)):
    z      = np.dot(X[i], w) + b
    y_pred = 1 if z > 0 else 0
    print(f"  x={X[i]} → z={z:.2f} → pred={y_pred} → actual={y[i]}")