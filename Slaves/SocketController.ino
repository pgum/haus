#include <RCSwitch.h>

class RelayController{
  short int InputPins[2];
public:
  RelayController(){}
  
  void turnOn(short int input){
    digitalWrite(InputPins[input], LOW);
  }
  
  void turnOff(short int input){
    digitalWrite(InputPins[input], HIGH);
  }
  
  void initRelayController(short int in1pin, short int in2pin){
    InputPins[0]=in1pin;
    InputPins[1]=in2pin;
    pinMode(InputPins[0], OUTPUT);
    pinMode(InputPins[1], OUTPUT);
  }
};

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
RelayController relayc;
void setup() {
    // Transmitter is connected to Arduino Pin #10  
    sc.initSocketController(10);
    relayc.initRelayController(8,7);
    Serial.begin(9600);
}

void printAction(char* device ,short socketId, char* state){
    delay(100);
    Serial.print(device);
    Serial.print(socketId);
    Serial.print(" should be ");
    Serial.println(state);
  }

  const String light="l";
  const String relay="r";
    
  const String turnOn="n";
  const String turnOff="f";    
  
void loop() {
  String line="";
  if(Serial.available()){
    line = Serial.readStringUntil(';');
  }
    String device=String(line[0]);
    String command=String(line[1]);
    String channel=String(line[2]);
  if(device == light){
    if(command == turnOn){
      sc.turnOn(channel.toInt());
      printAction("(LIGHT)",channel.toInt(), "On");
    }
    if(command == turnOff){
      sc.turnOff(channel.toInt());
      printAction("(LIGHT)",channel.toInt(), "Off");
    }  
  }
  if(device == relay){
    if(command == turnOn){
      relayc.turnOn(channel.toInt());
      printAction("(RELAY)",channel.toInt(), "On");
    }
    if(command == turnOff){
      relayc.turnOff(channel.toInt());
      printAction("(RELAY)",channel.toInt(), "Off");
    }
  }
  delay(10);
  
}
