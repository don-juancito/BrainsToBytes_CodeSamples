def neural_network(input, weight):
    predicted_value = input * weight
    return predicted_value


minutes_running = 20
actual_calories_burned = 180

# We perform this extra assignment just to keep consistency with the names
input = minutes_running
expected_value = actual_calories_burned

weight = 7

predicted_value = neural_network(input, weight)

print("According to my neural network, I burned {} calories".format(predicted_value))


error = (predicted_value - expected_value)**2
print("The error in the prediction is {} ".format(error))



learning_rate = 0.1

prediction_upwards = neural_network(input, weight + learning_rate)
error_upwards = (prediction_upwards - expected_value)**2
print("The prediction with an updated weight of {} has an error of {}".format(weight+learning_rate, error_upwards))

prediction_downwards = neural_network(input, weight - learning_rate)
error_downwards = (prediction_downwards - expected_value)**2
print("The prediction with an updated weight of {} has an error of {}".format(weight-learning_rate, error_downwards))