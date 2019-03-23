class Antenna
    attr_accessor :length_in_meters
    def initialize(length_in_meters)
        @length_in_meters = length_in_meters
    end

    def send_information(information)
        # code for sending information using the antenna
        puts information
    end

    # Other methods and important things
end