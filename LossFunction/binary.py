import math

def binary_cross_entropy(actual, predicted):
    total = 0
    for a, p in zip(actual, predicted):
        total += a * math.log(p) + (1 - a) * math.log(1 -p)    # hint: a * math.log(p) + (1-a) * math.log(1-p)
    return -1 * (total / len(actual))   # negative to make positive

#test for good network  
actual    = [1.0, 0.0, 1.0]
predicted = [0.9, 0.1, 0.8]

loss = binary_cross_entropy(actual, predicted)
print(f"BCE Loss: {loss}") 


#test for badd network
predicted2 = [0.1, 0.9, 0.2]
loss2 = binary_cross_entropy(actual , predicted2)
print(f"BCF Loss : {loss2}")