import math
def sigmoid(x):
  return 1 / (1 + math.exp(-x))

def neron_with_sigmoid(i, w, b):
    raw =  sum(x * w for x , w in zip(i,w)) + b
    return sigmoid(raw)

input_weights = [1,2,3]
weight = [0.1,0.2,0.3]
bias = 1
sigmoid_output = neron_with_sigmoid(input_weights , weight , bias)
print(sigmoid_output)# raw = 2.4
# sigmoid(2.4) = 0.916 → 91.6% confidence → strongly YES 