def neural_network(input, weight):
    predicted_value = input * weight
    return predicted_value


input = 0.2
expected_value = 8
weight = 10

while True:
    # Because of how python handles floating point, we round the values
    predicted_value = round(neural_network(input, weight), 2)
    print("According to my neural network, the result is {}".format(predicted_value))
    error = (predicted_value - expected_value)**2
    print("The error in the prediction is {} ".format(error))

    derivative = input * (predicted_value - expected_value)
    print("The value of our derivative at weight={} is {}".format(weight, derivative))

    alpha = 24
    weight_adjustment = alpha * derivative
    
    weight -= weight_adjustment
    print("The new value of our weight is {}".format(weight))
    
    print("\n")
    if(error == 0):
        break