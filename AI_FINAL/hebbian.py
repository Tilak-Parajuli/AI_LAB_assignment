import numpy as np

# initial values
INPUTS = np.array([[1, 1], [1, -1], [-1, 1], [-1, -1]])


# step function (activation function)
def step_function(sum):
    if sum >= 0:
        return 1
    return -1


# calculateing output
def calculate_output(weights, instance, bias):
    sum = instance.dot(weights)+ bias #dot product
    return step_function(sum)
def hebb(outputs, weights, bias):
    for i in range(4):
        weights[0] = weights[0] + (INPUTS[i][0] * outputs[i])
        weights[1] = weights[1] + (INPUTS[i][1] * outputs[i])
        bias = bias + (1 * outputs[i])
        print("Weight updated: " + str(weights[0]))
        print("Weight updated: " + str(weights[1]))
        print("Bias updated: " + str(bias))
        print("----------------------------------------")
    return weights, bias
if __name__ == "__main__":
    and_outputs = np.array([1, -1, -1, -1])
    weights = np.array([0.0, 0.0])
    bias = 0
    returned_weights, returned_bias = hebb(and_outputs, weights, bias)
    print('predicted output[1, 1]: ' + str(calculate_output(returned_weights, np.array([[1, 1]]), returned_bias)))
    print('predicted output [1, -1]: ' + str(calculate_output(returned_weights, np.array([[1, -1]]), returned_bias)))
    print('predicted output [-1, 1]: ' + str(calculate_output(returned_weights, np.array([[-1, 1]]), returned_bias)))
    print('predicted output [-1, -1]: ' + str(calculate_output(returned_weights, np.array([[-1, -1]]), returned_bias)))
