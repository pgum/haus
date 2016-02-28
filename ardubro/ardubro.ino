#include <RCSwitch.h>
int LightSwitchPin = 11;

//TODO: change to template class
class RelayController{
public:
  short int InputPins[2];
  short int status[2];
  RelayController(){
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

//unsigned long RelayTurnOnCodes[]={1381457};
//unsigned long RelayTurnOffCodes[]={1381460};

unsigned long RelayTurnOnCodes[]={5201};
unsigned long RelayTurnOffCodes[]={5471};
RelayController relayController= RelayController();

  bool isCodeToTurnOn(unsigned long code){
      Serial.print("Turn On code: ");
      Serial.println( RelayTurnOnCodes[0]);
      Serial.print("Code 2 check: ");
      Serial.println( code);
      return RelayTurnOnCodes[0] == code;
  }
  bool isCodeToTurnOff(unsigned long code){
      Serial.print("Turn Off code: ");
      Serial.println( RelayTurnOffCodes[0]);
      Serial.print("Code to check: ");
      Serial.println( code);
      return RelayTurnOffCodes[0] == code;
  }


void setup(){
  Serial.begin(9600);
  relayController.initController(8,9);
  rcReceiver.enableReceive(4);  // INT4 is on Pin7
  pinMode(LightSwitchPin, INPUT_PULLUP);
}
bool switchState=false;
bool statusToSetAtTheEnd[2]={false,false};
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
      if(isCodeToTurnOn(value)){ statusToSetAtTheEnd[0]=true;}
      if(isCodeToTurnOff(value)){ statusToSetAtTheEnd[0]=false;}
    }
    rcReceiver.resetAvailable();
  }
  bool lastState= switchState;
  switchState = digitalRead(LightSwitchPin);
  //relayController.turn(0, switchState);
  if(lastState != switchState){
    Serial.print("Switch changed from:");
    Serial.print(lastState);
    Serial.print(" to:");
    Serial.println(switchState);
    statusToSetAtTheEnd[0]=switchState;
  }

  for(int i=0; i<2; ++i){
    relayController.turn(i, statusToSetAtTheEnd[i]);
  }
}
