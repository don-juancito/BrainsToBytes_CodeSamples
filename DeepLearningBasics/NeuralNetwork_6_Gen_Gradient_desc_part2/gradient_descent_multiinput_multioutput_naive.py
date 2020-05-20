def dot_product(first_vector, second_vector):
    assert( len(first_vector) == len(second_vector))

    vectors_size = len(first_vector)
    dot_product_result = 0

    for index in range(vectors_size):
        dot_product_result += first_vector[index] * second_vector[index]

    return round(dot_product_result, 2)


def multi_input_multi_output_neural_network(inputs, weights):
    predicted_values= []
    
    for weights_for_estimate in weights:
        predicted_values.append( dot_product(inputs, weights_for_estimate) )

    return predicted_values

alpha = 0.2
inputs = [0.2, 2.3, 1.2]
expected_values = [8, 46, 0.1]

weights_1 = [7.1, 1.1, 4.4] # Weights for the first output
weights_2 = [5.7, 3, 9.1]   # Weights for the second output
weights_3 = [2.2, 5.3, 7]   # Weights for the third output

weights = [weights_1, weights_2,  weights_3]

while True:
    predicted_values = multi_input_multi_output_neural_network(inputs, weights)
    print("According to my neural network, the 1st result is {}".format(predicted_values[0]))
    print("According to my neural network, the 2nd result is {}".format(predicted_values[1]))
    print("According to my neural network, the 3rd result is {}".format(predicted_values[2]))

    error_1 = (predicted_values[0] - expected_values[0])**2
    error_2 = (predicted_values[1] - expected_values[1])**2
    error_3 = (predicted_values[2] - expected_values[2])**2

    print("The error in the 1st prediction is {} ".format(error_1))
    print("The error in the 2nd prediction is {} ".format(error_2))
    print("The error in the 3rd prediction is {} ".format(error_3))

    ## These weights participated in the prediction of the first output value
    weight_adjustment_1 = alpha * inputs[0] * (predicted_values[0] - expected_values[0])
    weight_adjustment_2 = alpha * inputs[1] * (predicted_values[0] - expected_values[0])
    weight_adjustment_3 = alpha * inputs[2] * (predicted_values[0] - expected_values[0])
    weights[0][0] -= weight_adjustment_1
    weights[0][1] -= weight_adjustment_2
    weights[0][2] -= weight_adjustment_3

    print("\n")
    print("The 1st weight for the first output is now {} ".format(weights[0][0]) )
    print("The 2nd weight for the first output is now {} ".format(weights[0][1]) )
    print("The 3rd weight for the first output is now {} ".format(weights[0][2]) )

    ## These weights participated in the prediction of the second output value
    weight_adjustment_4 = alpha * inputs[0] * (predicted_values[1] - expected_values[1])
    weight_adjustment_5 = alpha * inputs[1] * (predicted_values[1] - expected_values[1])
    weight_adjustment_6 = alpha * inputs[2] * (predicted_values[1] - expected_values[1])
    weights[1][0] -= weight_adjustment_4
    weights[1][1] -= weight_adjustment_5
    weights[1][2] -= weight_adjustment_6

    print("\n")
    print("The 1st weight for the second output is now {} ".format(weights[1][0]) )
    print("The 2nd weight for the second output is now {} ".format(weights[1][1]) )
    print("The 3rd weight for the second output is now {} ".format(weights[1][2]) )

    ## These weights participated in the prediction of the third output value
    weight_adjustment_7 = alpha * inputs[0] * (predicted_values[2] - expected_values[2])
    weight_adjustment_8 = alpha * inputs[1] * (predicted_values[2] - expected_values[2])
    weight_adjustment_9 = alpha * inputs[2] * (predicted_values[2] - expected_values[2])
    weights[2][0] -= weight_adjustment_7
    weights[2][1] -= weight_adjustment_8
    weights[2][2] -= weight_adjustment_9

    print("\n")
    print("The 1st weight for the third output is now {} ".format(weights[2][0]) )
    print("The 2nd weight for the third output is now {} ".format(weights[2][1]) )
    print("The 3rd weight for the third output is now {} ".format(weights[2][2]) )

    print("\n")
    #We stop when all errors are 0
    if(error_1 + error_2 + error_3 == 0):
        break