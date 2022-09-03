import numpy as np

# initial values
INPUTS = np.array([[1, 1], [1, -1], [-1, 1], [-1, -1]])
LEARNING_RATE = 0.1


# step function (activation function)
def step_function(sum):
    if sum >= 0:
        return 1
    return -1


# calculateing output
def calculate_output(weights, instance, bias):
    sum = instance.dot(weights) + bias
    return step_function(sum)
def perceptron(outputs, weights, bias):
    total_error = 1
    counter = 0
    while total_error != 0 and counter < 10:

        total_error = 0
        counter += 1
        for i in range(len(outputs)):
            sum = INPUTS[i].dot(weights)
            prediction = step_function(sum + bias)

            total_error += outputs[i] - prediction

            if outputs[i] != prediction:
                weights[0] = weights[0] + (LEARNING_RATE * outputs[i] * INPUTS[i][0])
                weights[1] = weights[1] + (LEARNING_RATE * outputs[i] * INPUTS[i][1])
                bias = bias + (LEARNING_RATE * outputs[i])
                print("Weight updated: " + str(weights[0]))
                print("Weight updated: " + str(weights[1]))
                print("Bias updated: " + str(bias))
                print("----------------------------------------")

        print("Total error: " + str(total_error))
        print("----------------------------------------")

    return weights, bias
if __name__ == "__main__":
    and_outputs = np.array([1, -1, -1, -1])
    weights = np.array([0.0, 0.0])
    bias = 0

    returned_weights, returned_bias = perceptron(and_outputs, weights, bias)
    print('predicted output for [1, 1]: ' + str(calculate_output(returned_weights, np.array([[1, 1]]), returned_bias)))
    print('predicted output [1, -1]: ' + str(calculate_output(returned_weights, np.array([[1, -1]]), returned_bias)))
    print('predicted output [-1, 1]: ' + str(calculate_output(returned_weights, np.array([[-1, 1]]), returned_bias)))
    print('predicted output [-1, -1]: ' + str(calculate_output(returned_weights, np.array([[-1, -1]]), returned_bias)))
