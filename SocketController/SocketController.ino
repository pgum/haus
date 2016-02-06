#include <RCSwitch.h>

void printAction(short socketId, char* state){
    delay(100);
    Serial.print(socketId);
    Serial.print(" should be ");
    Serial.print(state);
  }

class SocketController{
  RCSwitch rc;
  char* homePin="10001";
  char* ch[][]={"10000", "01000", "00100", "00010"};
  public:
  SocketController(){}

  void initSocketController(int transmitterPin){
    rc.enableTransmit(transmitterPin);
    rc.setPulseLength(320); // Optional set pulse length.
  }
  void turnOn(short int socketId){
    mySwitch.switchOn(homePin, ch[socketId] );
  }
  void turnOff(short int socketId){
    mySwitch.switchOff(homePin, ch[socketId] );
  }
};

SocketController sc;
void setup() {
    // Transmitter is connected to Arduino Pin #10  
    sc.initSocketController(10);

    Serial.begin(9600);
}

  const String turnOn="+";
  const String turnOff="-";    
  String command="";
  int commandLength= command.length();
void loop() {
  
  if(Serial.available()){
    command = Serial.readStringUntil(';');
  }
  Serial.print(command.lenght());
  /*
  if(str[0] == turnOn){
    sc.turnOn(str[1].toInt());
    printAction(str[1], "On");
  }
  if(str[0] == turnOff){
    sc.turnOff(str[1].toInt());
  }
  */
  delay(10);
}
