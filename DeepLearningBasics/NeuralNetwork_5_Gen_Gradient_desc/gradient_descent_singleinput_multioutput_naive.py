def neural_network(input, weight):
    predicted_value = input * weight
    return predicted_value
    
input = 0.2
expected_value_1 = 8
expected_value_2 = 46
expected_value_3 = 0.1

weight_1 = 10
weight_2 = 20
weight_3 = 3

while True:
    # Because of how python handles floating point, we round the values
    predicted_value_1 = round(neural_network(input, weight_1), 2)
    predicted_value_2 = round(neural_network(input, weight_2), 2)
    predicted_value_3 = round(neural_network(input, weight_3), 2)

    print("According to my neural network, the 1st result is {}".format(predicted_value_1))
    print("According to my neural network, the 2nd result is {}".format(predicted_value_2))
    print("According to my neural network, the 3rd result is {}".format(predicted_value_3))

    error_1 = (predicted_value_1 - expected_value_1)**2
    error_2 = (predicted_value_2 - expected_value_2)**2
    error_3 = (predicted_value_3 - expected_value_3)**2

    print("The error in the 1st prediction is {} ".format(error_1))
    print("The error in the 2nd prediction is {} ".format(error_2))
    print("The error in the 3rd prediction is {} ".format(error_3))

    derivative_1 = input * (predicted_value_1 - expected_value_1)
    derivative_2 = input * (predicted_value_2 - expected_value_2)
    derivative_3 = input * (predicted_value_3 - expected_value_3)

    print("The value of our derivative for the 1st weight={} is {}".format(weight_1, derivative_1))
    print("The value of our derivative for the 2nd weight={} is {}".format(weight_2, derivative_2))
    print("The value of our derivative for the 3rd weight={} is {}".format(weight_3, derivative_3))


    alpha = 24

    weight_adjustment_1 = alpha * derivative_1
    weight_adjustment_2 = alpha * derivative_2
    weight_adjustment_3 = alpha * derivative_3
    
    weight_1 -= weight_adjustment_1
    weight_2 -= weight_adjustment_2
    weight_3 -= weight_adjustment_3

    print("The new value of our 1st weight is {}".format(weight_1))
    print("The new value of our 2nd weight is {}".format(weight_2))
    print("The new value of our 3rd weight is {}".format(weight_3))        
    
    print("\n")
    #We stop when all errors are 0
    if(error_1 + error_2 + error_3 == 0):
        break