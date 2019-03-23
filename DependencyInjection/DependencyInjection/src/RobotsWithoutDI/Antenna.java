package RobotsWithoutDI;

public class Antenna {
    private int lengthInMeters;

    public Antenna(double lengthInMeters){
        lengthInMeters = lengthInMeters;
    }

    public void sendInformation(String information){
//      Code for sending information using the antenna
        System.out.println(information);
    }

//  Other methods and important things
}
