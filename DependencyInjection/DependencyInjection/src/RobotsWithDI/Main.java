package RobotsWithDI;

public class Main {

    public static void main(String[] args) {
        InverterWire wire= new InverterWire();
        Robot robbie = new Robot("awesomebot", "awb-46465", wire);
        robbie.sendRobotInformation();
    }
}
