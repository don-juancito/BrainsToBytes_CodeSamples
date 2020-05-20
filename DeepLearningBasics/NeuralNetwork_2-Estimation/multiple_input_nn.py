
# Now, input and information are both number arrays
def multi_input_neural_network(input_information, weights):
    assert( len(input_information) == len(weights))

    calories_burned = 0
    for index in range(len(weights)):
        calories_burned += input_information[index] * weights[index]

    return calories_burned


#DEMO

# Inputs is an array, ordered as: minutes jogging --> jogging speed ---> mass of the runner
# Minutes jogging: 30
# Jogging speed: 3 m/s
# Runner's mass: 80kg
inputs = [30, 3, 80]

# The weights array follows the same order
calculated_weights = [6.2, 8.1, 0.31]

calories_burned = multi_input_neural_network(inputs, calculated_weights )

print("According to my neural network, I burned {} calories".format(calories_burned))