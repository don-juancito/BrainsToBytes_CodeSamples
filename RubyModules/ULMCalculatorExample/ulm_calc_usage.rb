require_relative 'uniform_linar_motion_calculator'

ULMCalculator.calculate_speed(distance_in_meters: 100, 
                              time_in_seconds: 5)
                              
ULMCalculator.calculate_distance(speed: 100, 
                                 time_in_seconds: 10)

ULMCalculator.calculate_time(distance_in_meters: 100, 
                             speed: 25)