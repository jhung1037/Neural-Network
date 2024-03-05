import random
import numpy as np

# input = [round(random.uniform(-1.0, 1.0), 1) for _ in range(4)]
input = [[round(random.uniform(-1.0, 1.0), 1) for _ in range(4)] for _ in range(3)]
weights = [[round(random.uniform(-1.0, 1.0), 2) for _ in range(4)] for _ in range(3)]
biases = [round(random.uniform(-1.0, 1.0), 1) for _ in range(3)]
# print(input, weights, biases)

weights2 = [[round(random.uniform(-1.0, 1.0), 2) for _ in range(3)] for _ in range(3)]
biases2 = [round(random.uniform(-1.0, 1.0), 1) for _ in range(3)]

#output = np.dot(weights, input) + biases # not dot(input, weights)
layer1_output = np.dot(input, np.array(weights).T) + biases
layer2_output = np.dot(layer1_output, np.array(weights2).T) + biases2 
print(layer2_output)