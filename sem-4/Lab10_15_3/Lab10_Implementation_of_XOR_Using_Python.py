#Import the necessary library
import numpy as np
#np.random.seed(0)


def sigmoid(x):
    """Implementing the sigmoid function for x.
    sig(x) = 1/(1+e^-x)

    Args:
        x: input for which signmoid function needs to be calculated.

    Returns:
        the sigmoid function.
    """
    return 1 / (1 + (np.exp(-x)))


def sigmoid_derivative(x):
    """Implementing the sigmoid function for x.
    sig'(x) = x * (1-x)

    Args:
        x: input for which derivative of signmoid function needs to be calculated.

    Returns:
        the derivative of sigmoid function.
    """
    return x * (1-x)


outputs = {'and': [[0], [0], [0], [1]], 'nand': [[1], [1], [1], [0]], 'or': [[1], [1], [1], [0]],
           'nor': [[0], [0], [0], [1]], 'xor': [[0], [1], [1], [0]], 'xnor': [[1], [0], [0], [1]], }
input_list = [(0, 0), (0, 1), (1, 0), (1, 1)]

lg = """
█░░ █▀▀█ █▀▀▀ ░▀░ █▀▀ 　 █▀▀▀ █▀▀█ ▀▀█▀▀ █▀▀ █▀▀ 
█░░ █░░█ █░▀█ ▀█▀ █░░ 　 █░▀█ █▄▄█ ░░█░░ █▀▀ ▀▀█ 
▀▀▀ ▀▀▀▀ ▀▀▀▀ ▀▀▀ ▀▀▀ 　 ▀▀▀▀ ▀░░▀ ░░▀░░ ▀▀▀ ▀▀▀
A B | AND NAND OR NOR XOR XNOR
-------------------------------
0 0 |  0    1   0  1   0   1
0 1 |  0    1   1  0   1   0
1 0 |  0    1   1  0   1   0
1 1 |  1    0   1  0   0   1
"""
print(lg)

while True:
    try:
        output_list = outputs[input('Enter your chosen logic gate: ').lower()]
        break
    except KeyError:
        print('Invalid logic gate, try again!\n')


#Set the Input datasets
inputs = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
#Set the expected output
expected_output = np.array(output_list)


# Set the epochs
epochs = 100000
# Set the learning rate
lr = 0.1
# Set the number of neuron at input layer, hidden layer and output layers
inputLayerNeurons = 2
hiddenLayerNeurons = 2
outputLayerNeurons = 1


# Random weights and bias initialization
# Initialize the uniform distribution to hiddent weight as (inputLayerNeurons,hiddenLayerNeurons)
hidden_weights = np.random.uniform(
    size=(inputLayerNeurons, hiddenLayerNeurons))
# Initialize the uniform distribution to hiddent bias as (1,hiddenLayerNeurons)
hidden_bias = np.random.uniform(size=(1, hiddenLayerNeurons))
# Initialize the uniform distribution to output weight as (hiddenLayerNeurons,outputLayerNeurons)
output_weights = np.random.uniform(
    size=(hiddenLayerNeurons, outputLayerNeurons))
# Initialize the uniform distribution to output bias as (1,outputLayerNeurons)
output_bias = np.random.uniform(size=(1, outputLayerNeurons))


# Display the hidden_weights, hidden_bias, output_weights, and output_bias
print("Initial hidden weights: ", end='')
print(*hidden_weights)
print("Initial hidden biases: ", end='')
print(*hidden_bias)
print("Initial output weights: ", end='')
print(*output_weights)
print("Initial output biases: ", end='')
print(*output_bias)


# Training algorithm
# Iterate over epochs
for _ in range(epochs):
    # Forward Propagation
    # Perform the dot operations between inputs and hidden_weights. Use np.dot() function
    hidden_layer_activation = np.dot(inputs, hidden_weights)
    hidden_layer_activation += hidden_bias
    # Call the sigmoid method for hidden_layer_activation
    hidden_layer_output = sigmoid(hidden_layer_activation)

    # Perform the dot operations between hidden_layer_output and output_weights. Use np.dot() function
    output_layer_activation = np.dot(hidden_layer_output, output_weights)
    output_layer_activation += output_bias
    # Call the sigmoid method for output_layer_activation
    predicted_output = sigmoid(output_layer_activation)

    # Backpropagation
    # Calculate the error by performing (expected_output - predicted_output)
    error = expected_output - predicted_output
    # Calculate the derivate of predicted output by performing error * sigmoid_derivative(predicted_output)
    d_predicted_output = error * sigmoid_derivative(predicted_output)

    error_hidden_layer = d_predicted_output.dot(output_weights.T)

    # Calculate the derivate of hidden layer by performing error_hidden_layer * sigmoid_derivative(hidden_layer_output)
    d_hidden_layer = error_hidden_layer * \
        sigmoid_derivative(hidden_layer_output)

    # Updating Weights and Biases
    # Update the output weights as output_weights = output_weights + hidden_layer_output.T.dot(d_predicted_output) * lr
    output_weights = output_weights + \
        hidden_layer_output.T.dot(d_predicted_output) * lr
    output_bias += np.sum(d_predicted_output, axis=0, keepdims=True) * lr
    # Update the hidden weights as hidden_weights = height_weights + inputs.T.dot(d_hidden_layer) * lr
    hidden_weights = hidden_weights + inputs.T.dot(d_hidden_layer) * lr
    hidden_bias += np.sum(d_hidden_layer, axis=0, keepdims=True) * lr


# Display the hidden_weights, hidden_bias, output_weights and output_bias after training
print("Final hidden weights: ", end='')
print(*hidden_weights)
print("Final hidden bias: ", end='')
print(*hidden_bias)
print("Final output weights: ", end='')
print(*output_weights)
print("Final output bias: ", end='')
print(*output_bias)


# The predicted output
print(f"\nOutput from neural network after {epochs} epochs: ", end='')
print(*predicted_output)
