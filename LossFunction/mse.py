def mse(actual, predicted):
    total = 0
    for a, p in zip(actual, predicted):
        total += (a - p) ** 2       # squared difference
    return total / len(actual)      # divide by number of items

# Test with good value
actual    = [1.0, 0.0, 1.0]
predicted = [0.9, 0.1, 0.8]

loss = mse(actual, predicted)
print(f"MSE Loss: {loss}\n")   # good network → 0.02 , netwrok was nearly right -> small loss


# Bad predictions — far from actual
actual2    = [1.0, 0.0, 1.0]
predicted2 = [0.1, 0.9, 0.2]

loss2 = mse(actual2 , predicted2)
print(f"MSE Loss  : {loss2}\n") # Bad network  → 0.75  Network was nearly wrong  → large loss