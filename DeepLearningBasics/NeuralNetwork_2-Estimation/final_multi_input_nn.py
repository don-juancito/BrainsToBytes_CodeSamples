def dot_product(first_vector, second_vector):
    assert( len(first_vector) == len(second_vector))

    vectors_size = len(first_vector)
    dot_product_result = 0

    for index in range(vectors_size):
        dot_product_result += first_vector[index] * second_vector[index]

    return dot_product_result

def multi_input_neural_network(input_information, weights):
    calories_burned = dot_product(input_information, weights)
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