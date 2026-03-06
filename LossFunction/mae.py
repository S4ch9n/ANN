
def mae(a,p):
  total = 0
  for a , p in zip(a,p):
    total += abs(a-p) #absoulte difference 

  return total / len(a)  

# Test with same data
actual    = [1.0, 0.0, 1.0]
predicted = [0.9, 0.1, 0.8]

loss = mae(actual , predicted)
print(loss)
