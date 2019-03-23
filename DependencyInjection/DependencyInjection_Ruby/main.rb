require_relative 'robot'
require_relative 'antenna'

antenna = Antenna.new(7)
robbie = Robot.new("awesomebot", "46465", antenna)
robbie.send_robot_information();