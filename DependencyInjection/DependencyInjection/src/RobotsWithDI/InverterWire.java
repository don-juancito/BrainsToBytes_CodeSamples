package RobotsWithDI;

public class InverterWire implements MessageSender{

    public InverterWire(){
    }

    public void sendInformation(String information){
//        Code to send information using the antenna
        System.out.println(new StringBuilder(information).reverse().toString());
    }

//    Other methods and important things
}
