def simple_neural_network(input_information, weight):
    return input_information * weight


calculated_weight = 7.56
minutes_jogging = 30 

calories_burned = simple_neural_network(minutes_jogging, calculated_weight )

print("According to my neural network, after running {} minutes, I burned {} calories".format(minutes_jogging, calories_burned))