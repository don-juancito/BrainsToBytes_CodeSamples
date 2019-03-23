class Robot
    attr_accessor :model, :serial, :message_sender
    def initialize(model, serial, message_sender)
        @model = model
        @serial = serial
        @message_sender = message_sender
    end

    def send_robot_information
        robot_info = get_robot_information();
        message_sender.send_information(robot_info)
    end

    # Other important methods
    private

    def get_robot_information
        "Model: #{model} \nSerial: #{serial}"
    end
end