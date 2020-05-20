def neural_network_multi_output(input, weights):
    predicted_values = []
    for  weight in weights:
        predicted_value = round( input * weight, 2)
        predicted_values.append(predicted_value)

    return predicted_values

def calculate_errors(predicted_values, expected_values):
    errors = []
    for pred_value, exp_value in zip(predicted_values, expected_values):
        error = (pred_value - exp_value)**2
        errors.append(error)
    
    return errors

def calculate_weight_adjustments(alpha, input, predicted_values, expected_values):
    weight_adjustments = []

    for pred_value, exp_value in zip(predicted_values, expected_values):
        weight_adjustment = alpha * input * (pred_value- exp_value)
        weight_adjustments.append(weight_adjustment)

    return weight_adjustments

def calculate_updated_weights(weights, weight_adjustments):
    updated_wights = []

    for weight, weight_adjustment in zip(weights, weight_adjustments):
        updated_wight = weight - weight_adjustment
        updated_wights.append(updated_wight)

    return updated_wights


input = 0.2
alpha = 24

expected_values = [8, 46, 0.1]
weights = [10, 20, 3]

while True:
    # Because of how python handles floating point, we round the values
    predicted_values = neural_network_multi_output(input, weights)

    print("According to my neural network, the 1st result is {}".format(predicted_values[0]))
    print("According to my neural network, the 2nd result is {}".format(predicted_values[1]))
    print("According to my neural network, the 3rd result is {}".format(predicted_values[2]))

    errors = calculate_errors(predicted_values, expected_values)

    print("The error in the 1st prediction is {} ".format(errors[0]))
    print("The error in the 2nd prediction is {} ".format(errors[1]))
    print("The error in the 3rd prediction is {} ".format(errors[2]))

    weight_adjustments = calculate_weight_adjustments(alpha, input, predicted_values, expected_values)

    weights = calculate_updated_weights(weights, weight_adjustments)
    
    print("The new value of our 1st weight is {}".format(weights[0]))
    print("The new value of our 2nd weight is {}".format(weights[1]))
    print("The new value of our 3rd weight is {}".format(weights[2]))        
    
    print("\n")
    #We stop when all errors are 0
    if(errors[0] + errors[1] + errors[2] == 0):
        break