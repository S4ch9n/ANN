def relu(x):
  return max(0 , x)

def neuron_with_relu(i , w , b):
  raw =  sum(x * w for x , w in zip(i,w)) + b
  return relu(raw)

input_data = [1,2,3]
weight = [0.1,0.2,0.3]
bias  = 1
relu_output = neuron_with_relu(input_data , weight, bias)
print(f"final output : {relu_output}")

#relu blocking negative value
print("___---relu blocking negative value---___")
bias2 = -10
relu_output2 = neuron_with_relu(input_data , weight , bias2)
print(f"final output : {relu_output2}")