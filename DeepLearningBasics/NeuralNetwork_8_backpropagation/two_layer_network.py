import numpy as nmpy

# These methods run over numpy arrays
def relu(x):
    return (x > 0) * x

def relu_deriv(prev_output):
    return prev_output > 0

# Variable setup: we use numpy's array to create a more concise implementation
alpha = 0.1
hidden_layer_number_of_nodes = 4

weights_1 = nmpy.random.random((3 ,hidden_layer_number_of_nodes))
weights_2 = nmpy.random.random((hidden_layer_number_of_nodes))

inputs = nmpy.array([[1,1,1],
                     [1,1,0],
                     [0,1,0],
                     [0,1,1]
                    ])

expected_values = nmpy.array([1,0,1,0])

run = 0
while True:
    overall_run_error = 0

    for input_set, expected_value in zip(inputs, expected_values):
        # These are the outputs of the intermediate layer (the one with 4 nodes)
        hidden_outputs = relu( nmpy.dot(input_set, weights_1) )
        # This is the final output, this concludes the prediction process
        predicted_value = round(nmpy.dot(hidden_outputs, weights_2), 1)

        # Now, we calculate the deltas and update the weights using
        # the logic we previously described
        layer2_delta = (predicted_value - expected_value)
        # relu_deriv makes sure we only update nodes with output > 0
        layer1_delta = (weights_2 * layer2_delta) * relu_deriv(hidden_outputs)

        weights_2 -= alpha * hidden_outputs.dot(layer2_delta)
        weights_1 -= alpha * nmpy.outer(input_set, layer1_delta)

        # We calculate an accumulated error for every run
        overall_run_error += nmpy.sum((predicted_value-expected_value) ** 2)

    run += 1
    ## Let's print some debug data
    print("The weights in the final layer are: \n{}".format(weights_2) )
    print("The weights in the first layer are: \n{}".format(weights_1) )
    print("The overall error for the run {} is {}\n\n".format(run, overall_run_error))

    if overall_run_error == 0:
        break
