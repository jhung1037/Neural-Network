import math
import numpy as np

layer_outputs =[4.8, 1.21, 2.385]

# E = 2.71828182846
E = math.e

# exp_values = []

# for output in layer_outputs:
#     exp_values.append(E**output)
exp_values = np.exp(layer_outputs)
print(exp_values)

# norm_base = sum(exp_values)
# norm_values = []

# for value in exp_values:
#     norm_values.append(value / norm_base)
norm_values = exp_values / np.sum(exp_values)
print(norm_values)
print(sum(norm_values))