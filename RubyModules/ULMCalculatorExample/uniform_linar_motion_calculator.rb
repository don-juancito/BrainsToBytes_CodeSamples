module ULMCalculator
    # all speeds in m/s
    def self.calculate_speed(distance_in_meters:, time_in_seconds:)
        raise ArgumentError, "We can't calculate for time = 0" if time_in_seconds == 0 

        speed = distance_in_meters / time_in_seconds
        puts "An object that moves #{distance_in_meters}m in #{time_in_seconds}s has a speed of #{speed}m/s"
        return speed
    end

    def self.calculate_distance (speed:, time_in_seconds:)
        distance_in_meters = speed * time_in_seconds
        puts "An object with a speed of #{speed}m/s moving for #{time_in_seconds}s travels a distance of #{distance_in_meters}m"
        return distance_in_meters
    end

    def self.calculate_time(distance_in_meters:, speed:)
        raise ArgumentError, "We can't calculate for speed = 0" if speed == 0    
                           
        time_in_seconds = distance_in_meters / speed
        puts "It takes an object #{time_in_seconds}s to move #{distance_in_meters}m if it moves at #{speed}m/s"
        return time_in_seconds
    end
end
