package RobotsWithDI;

public class Robot {
    private String model;
    private String serial;
    private MessageSender messageSender;

    public Robot(String model, String serial, MessageSender messageSender){
        this.model = model;
        this.serial = serial;
        this.messageSender = messageSender;
    }

    public void sendRobotInformation(){
        String robotInfo = getRobotInformation();
        messageSender.sendInformation(robotInfo);
    }

    private String getRobotInformation(){
        String robotInfo = String.format("Model: %s\nSerial: %s", model, serial);
//        Any extra steps for gathering/formatting info
        return robotInfo;
    }

//    Other methods

}
