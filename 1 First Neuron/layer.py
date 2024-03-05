import random
import numpy as np
import dataset

np.random.seed(0)

# X = [[round(random.uniform(-1.0, 1.0), 1) for _ in range(4)] for _ in range(3)]

X, y = dataset.create_data(100, 3)

class Layer_Dense:
    def __init__(self, n_inputs, n_neurons) -> None:
        self.weights = 0.1 * np.random.randn(n_inputs, n_neurons)
        self.biases = np.zeros((1,n_neurons))
    def forward(self, inputs):
        self.output = np.dot(inputs, self.weights) + self.biases

class Activation_ReLU:
    def forward(self, inputs):
        self.output = np.maximum(0, inputs)

# layer1 = Layer_Dense(4,5)
# layer2 = Layer_Dense(5,2)

# layer1.forward(X)
# # print(layer1.output)
# layer2.forward(layer1.output)
# print(layer2.output)

# layer1 = Layer_Dense(2,5) # two features in the graph
# activation1 = Activation_ReLU()
# layer1.forward(X)
# activation1.forward(layer1.output)
# print(activation1.output)


class Activation_ReLU:
    def forward(self, inputs):
        self.output = np.maximum(0, inputs)

class Activation_Softmax:
    def forward(self, inputs):
        exp_values = np.exp(inputs - np.max(inputs, axis = 1, keepdims=True))
        probabilities = exp_values / np.sum(exp_values, axis = 1, keepdims=True)
        self.output = probabilities
    
dense1 = Layer_Dense(2,3)
activation1 = Activation_ReLU()
dense2 = Layer_Dense(3,3)
activation2 = Activation_Softmax()

dense1.forward(X)
activation1.forward(dense1.output)

dense2.forward(activation1.output)
activation2.forward(dense2.output)

# print(activation2.output[:5])


class Loss:
    def calculate(self, output, y):
        sample_losses = self.forward(output, y)
        data_loss = np.mean(sample_losses)
        return data_loss
    
class Loss_CategoricalCrossentropy(Loss):
    def forward(self, y_pred, y_true):
        samples = len(y_pred)
        y_pred_clipped = np.clip(y_pred, 1e-7, 1-1e-7)

        if len (y_true.shape) == 1:
            correct_confidences = y_pred_clipped[range(samples), y_true]
        elif len (y_true.shape) == 2:
            correct_confidences = np. sum(y_pred_clipped*y_true, axis=1)

        negative_log_likelihoods = -np.log(correct_confidences)
        return negative_log_likelihoods
    
loss_function = Loss_CategoricalCrossentropy()
loss = loss_function.calculate(activation2.output, y)

print('Loss:', loss)

predictions = np.argmax(activation2.output, axis=1)
accuracy = np.mean(predictions == y) # predictions == target_class
print ('Acc:', accuracy)