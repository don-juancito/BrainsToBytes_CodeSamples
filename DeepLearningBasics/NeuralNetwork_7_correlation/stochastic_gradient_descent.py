import numpy as nmpy

# Variable setup: we use numpy's array to create a more concise implementation
alpha = 0.1
weights = nmpy.array([0.5, 0.5, 0.5])

# The inputs and expected results are in corresponding order
inputs = nmpy.array([[0,0,1],
                     [0,1,0],
                     [1,1,1],
                     [0,1,1],
                     [1,0,0],
                     [1,0,1],
                     [0,0,0],
                     [1,1,0]
                    ])

expected_values = nmpy.array([0,1,1,1,0,0,0,1])

# Let's run the optimization for every input 15 times
for run in range(15):
    # This is the total error of a single run
    error_for_run = 0
    # Now we apply gradient descent to every pair of inputs/expected values
    for input_set, expected_value in zip(inputs, expected_values):

        # We can calculate our predicted value with a simple dot product operation, neat!
        predicted_value = round( input_set.dot(weights), 1)
        print("Our network predicted {} for the inputs {}".format(predicted_value, input_set))

        # Error calculation is the same as before, but with numpy magic!
        error = (predicted_value - expected_value) ** 2
        error_for_run += error

        # With the magic of numpy, updating weights is this easy!
        weights -= alpha * (input_set * (predicted_value - expected_value) )

    print("The accumulated error for this run is {} \n\n\n".format(error_for_run))

# TODO: Round the predicted value, and remove the weights print statement, and maybe, remove the weights rounding