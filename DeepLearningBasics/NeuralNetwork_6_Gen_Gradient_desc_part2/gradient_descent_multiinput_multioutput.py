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

def calculate_errors(predicted_values, expected_values):
    errors = []

    for predicted_value, expected_value in zip(predicted_values, expected_values):
        error = (predicted_value - expected_value)**2
        errors.append(error)

    return errors


def calculate_weight_correction_matrix(alpha, inputs, expected_values, predicted_values):
    weight_correction_factors = []

    #Calculates factors row for row
    for exp, pred in zip(expected_values, predicted_values):
        row = []
        delta = (pred - exp) * alpha
        
        for input in inputs:
            row.append( input * delta )

        weight_correction_factors.append(row)

    return weight_correction_factors

def calculate_corrected_weights(weights, correction_factors):
    updated_weights = []

    for row_weight, row_correction in zip(weights, correction_factors):
        row = []
        for weight, correction in zip(row_weight, row_correction):
            row.append( weight - correction )

        updated_weights.append(row)

    return updated_weights    

def calculate_total_error(errors):
    return sum(errors)


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

    errors = calculate_errors(predicted_values, expected_values)
    print("The error in the 1st prediction is {} ".format(errors[0]))
    print("The error in the 2nd prediction is {} ".format(errors[1]))
    print("The error in the 3rd prediction is {} ".format(errors[2]))

    ## These weights participated in the prediction of the first output value
    weight_correction_factors = calculate_weight_correction_matrix(alpha, inputs, expected_values, predicted_values)
    weights = calculate_corrected_weights(weights, weight_correction_factors)

    print("\n")
    print("The 1st weight for the first output is now {} ".format(weights[0][0]) )
    print("The 2nd weight for the first output is now {} ".format(weights[0][1]) )
    print("The 3rd weight for the first output is now {} ".format(weights[0][2]) )
    print("\n")
    print("The 1st weight for the second output is now {} ".format(weights[1][0]) )
    print("The 2nd weight for the second output is now {} ".format(weights[1][1]) )
    print("The 3rd weight for the second output is now {} ".format(weights[1][2]) )
    print("\n")
    print("The 1st weight for the third output is now {} ".format(weights[2][0]) )
    print("The 2nd weight for the third output is now {} ".format(weights[2][1]) )
    print("The 3rd weight for the third output is now {} ".format(weights[2][2]) )

    print("\n")
    #We stop when all errors are 0
    if(calculate_total_error(errors) == 0):
        break