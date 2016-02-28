#include <RCSwitch.h>
int LightSwitchPin = 11;

//TODO: change to template class
class RelayController{
public:
  short int InputPins[2];
  bool status[2];
  int RelayTurnOnCodes[2];
  int RelayTurnOffCodes[2];
  RelayController(){
    RelayTurnOnCodes[0]=12358; //TODO: move as parameter
    RelayTurnOnCodes[1]=5813; //TODO: move as parameter
    RelayTurnOffCodes[0]=8532; //TODO: move as parameter
    RelayTurnOffCodes[1]=3185; //TODO: move as parameter
    }

  bool checkCode(int code){
    for(int i=0; i<2; ++i){
      if(RelayTurnOnCodes[i] == code){
        turnOn(i); return true;}
      if(RelayTurnOffCodes[i] == code){
        turnOff(i); return true;}
    }
    return false;
  }

  void turn(short int input, bool state){
    status[input]=state;
    digitalWrite(InputPins[input], state);
  }

  void turnOn(short int input){
    turn(input, true);
  }

  void turnOff(short int input){
    turn(input, false);
  }
  void toggle(short int input){
    status[input]=!status[input];
    digitalWrite(InputPins[input], status[input]);
  }

  void initController(short int in1pin, short int in2pin){
    InputPins[0]=in1pin;
    InputPins[1]=in2pin;
    pinMode(InputPins[0], OUTPUT);
    pinMode(InputPins[1], OUTPUT);
    turnOff(0);
    turnOff(1);
  }
  String getStatus(){
    String reti="";
    for(int i=0; i<2; ++i){
      reti+= status[i] ? "n" : "f";
    }
    return reti;
  }
};


RCSwitch rcReceiver= RCSwitch();
RelayController relayController= RelayController();

void setup(){
  Serial.begin(9600);
  relayController.initController(8,9);
  rcReceiver.enableReceive(4);  // INT4 is on Pin7
  pinMode(LightSwitchPin, INPUT_PULLUP);
}
bool switchState;
void loop() {
  if(rcReceiver.available()) {
    int value= rcReceiver.getReceivedValue();
    if(value == 0) {
      Serial.print("Unknown encoding");
    } else {
      Serial.print("Received ");
      Serial.print( rcReceiver.getReceivedValue() );
      Serial.print(" / ");
      Serial.print( rcReceiver.getReceivedBitlength() );
      Serial.print("bit ");
      Serial.print("Protocol: ");
      Serial.println( rcReceiver.getReceivedProtocol() );
    }
    if(value > 0){
      relayController.checkCode(value);
    }
    rcReceiver.resetAvailable();
  }
  bool lastState= switchState;
  switchState = digitalRead(LightSwitchPin);
  relayController.turn(0, switchState);
  if(lastState != switchState){
    Serial.print("Switch changed from:");
    Serial.print(lastState);
    Serial.print(" to:");
    Serial.println(switchState);
  }
}
