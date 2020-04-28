def calculate_weight_adjustments(inputs, correction_factor):
    weight_adjustments = []

    for input in inputs:
        weight_adjustment = input * correction_factor
        weight_adjustments.append(weight_adjustment)

    return weight_adjustments


def calculate_updated_weights(weights, weight_adjustments):
    updated_wights = []

    for weight, weight_adjustment in zip(weights, weight_adjustments):
        updated_wight = weight - weight_adjustment
        updated_wights.append(updated_wight)

    return updated_wights


# Our trusty old multi-input neural network implementation
def multi_input_neural_network(inputs, weights):
    assert( len(inputs) == len(weights))

    predicted_value = 0
    for input, weight in zip(inputs, weights):
        predicted_value += input * weight

    return predicted_value

inputs = [0.2, 4, 0.1]
weights = [10, 2, 11]
expected_value = 8
alpha = 0.04

while True:
    # Because of how python handles floating point, we round the values
    predicted_value = round(multi_input_neural_network(inputs, weights), 2)
    print("According to my neural network, the result is {}".format(predicted_value))
    error = (predicted_value - expected_value)**2
    print("The error in the prediction is {} ".format(error))

    correction_factor = alpha  * (predicted_value - expected_value)
    weight_adjustments = calculate_weight_adjustments(inputs, correction_factor )
    print("These are the weight adjustment values: {}".format(weight_adjustments))

    weights = calculate_updated_weights(weights, weight_adjustments)
    print("These are the new weights: {}".format(weights))

    
    print("\n")
    if(error == 0):
        break