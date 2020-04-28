def dot_product(first_vector, second_vector):
    assert( len(first_vector) == len(second_vector))

    vectors_size = len(first_vector)
    dot_product_result = 0

    for index in range(vectors_size):
        dot_product_result += first_vector[index] * second_vector[index]

    return dot_product_result

def multi_input_multi_output_neural_network(input_information, weights):
    # Estimates will be put and returned in an array
    estimates = []
    
    for weights_for_estimate in weights:
        estimates.append( dot_product(input_information, weights_for_estimate) )

    return estimates


#DEMO

# Inputs is an array, ordered as: minutes jogging --> jogging speed ---> mass of the runner
# Minutes jogging: 30
# Jogging speed: 3 m/s
# Runner's mass: 80kg
inputs = [30, 3, 80]

# Weights for each of the 3 outputs
weights_for_calories = [6.2, 8.1, 0.31]
weights_for_extra_days = [0.00407, 0.00618, 0.00303]
weights_for_savings = [0.11, 0.23, 0.06]

# We combine all the weights in a single array to be fed in the neural network estimation function
all_weights = [weights_for_calories, weights_for_extra_days, weights_for_savings]

# The order of the results is the same as the order of weights calories -> extra days -> money saved
estimates = multi_input_multi_output_neural_network(inputs, all_weights )
print("According to my neural network, I burned {} calories".format(estimates[0]))
print("According to my neural network, I will live {} extra days".format(estimates[1]))
print("According to my neural network, I saved {} money units in hearth medication".format(estimates[2]))