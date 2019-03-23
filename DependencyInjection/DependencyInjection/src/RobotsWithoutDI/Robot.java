package RobotsWithoutDI;

public class Robot {
    private String model;
    private String serial;
    private Antenna antenna;

    public Robot(String model, String serial, double antennaLengthInMeters){
        this.model = model;
        this.serial = serial;
        antenna = new Antenna(antennaLengthInMeters);
    }

    public void sendRobotInformation(){
        String robotInfo = getRobotInformation();
        antenna.sendInformation(robotInfo);
    }

    private String getRobotInformation(){
        String robotInfo = String.format("Model: %s\nSerial: %s", model, serial);
//        Any extra steps for gathering/formatting info
        return robotInfo;
    }

//    Other methods

}
