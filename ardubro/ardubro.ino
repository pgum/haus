#include <RCSwitch.h>

int LightSwitchInterruptPin = 3;
volatile bool hasSwitchStateChanged= false;

void LightSwitchEvent(){
  hasSwitchStateChanged= true;
}

//TODO: change to template class
class RelayController{
  short int InputPins[2];
  bool status[2];
  int RelayTurnOnCodes[2];
  int RelayTurnOffCodes[2];
public:
  RelayController(){}

  void turnOn(short int input){
    status[input]=true;
    digitalWrite(InputPins[input], status[input]);
  }

  void turnOff(short int input){
    status[input]=false;
    digitalWrite(InputPins[input], status[input]);
  }
  void toggle(short int input){
    status[input]=!status[input];
    digitalWrite(InputPins[input], status[input]);
  }

  void initController(short int in1pin, short int in2pin){
    RelayTurnOnCodes={12358, 5813}; //TODO: move as parameter
    RelayTurnOffCodes={8532, 3185}; //TODO: move as parameter
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
};


RCSwitch rcReceiver= RCSwitch();
RelayController relayController= RelayController();

void setup(){
  Serial.begin(9600);
  relayController.initController(8,7);
  //rcReceiver.enableReceive(0);  // Receiver on interrupt 0 => that is pin #2
  attachInterrupt(digitalPinToInterupt(LightSwitchInterruptPin), LightSwitchEvent, CHANGE);
}

void loop() {
  if(false /*rc.available()*/) {

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
      for(int i=0; i<MAX_RELAYS; ++i){
        if(RelayTurnOnCodes[i] == value){
          relayController.turnOn(i);}
        if(RelayTurnOffCodes[i] == value){
          RelayController.turnOff(i);}
    }
    rcReceiver.resetAvailable();
  }

  if(hasSwitchStateChanged){
    Serial.print("Switch Has Changed!");
    relayController.toggle(0);
    hasSwitchStateChanged=false;

  }
}
