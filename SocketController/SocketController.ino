#include <RCSwitch.h>

void printAction(short socketId, char* state){
    delay(100);
    Serial.print(socketId);
    Serial.print(" should be ");
    Serial.println(state);
  }

class SocketController{
  RCSwitch rc;
  String homePin;//="10001";
  String ch[4];//[]={"10000", "01000", "00100", "00010"};
  public:
  SocketController(){
  homePin="10001";
  ch[0]="10000";
  ch[1]="01000";
  ch[2]="00100";
  ch[3]="00010";
  }

  void initSocketController(int transmitterPin){
    rc.enableTransmit(transmitterPin);
//    rc.setPulseLength(320); // Optional set pulse length.
  }
  void turnOn(short int socketId){
    rc.switchOn(homePin.c_str(), ch[socketId].c_str() );
  }
  void turnOff(short int socketId){
    rc.switchOff(homePin.c_str(), ch[socketId].c_str() );
  }
};

SocketController sc;
void setup() {
    // Transmitter is connected to Arduino Pin #10  
    sc.initSocketController(10);

    Serial.begin(9600);
}

  const String turnOn="n";
  const String turnOff="f";    
  
void loop() {
  String line="";
  if(Serial.available()){
    line = Serial.readStringUntil(';');
  }
    String command=String(line[0]);
    String channel=String(line[1]);
  
  if(command == turnOn){
    sc.turnOn(channel.toInt());
    printAction(channel.toInt(), "On");
  }
  if(command == turnOff){
    sc.turnOff(channel.toInt());
    printAction(channel.toInt(), "Off");
  }
  delay(10);
  
}
