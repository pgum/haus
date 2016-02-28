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

long int RelayTurnOnCodes[2]={1381457L,-1};
long int RelayTurnOffCodes[2]={1381460L,-1};
RelayController relayController= RelayController();

  short int checkCodeOn(int code){
    for(int i=0; i<2; ++i){
      if(RelayTurnOnCodes[i] == code){return i;}}
      return -1;
  }
  short int checkCodeOff(int code){
    for(int i=0; i<2; ++i){
      if(RelayTurnOffCodes[i] == code){return i;}}
      return -1;
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
      Serial.print("Check Code On: ");
      short int checkResult = checkCodeOn(value);
      Serial.println(checkResult);
      if(checkResult>=0){ statusToSetAtTheEnd[checkResult]=true;}
      Serial.print("Check Code Off: ");
      checkResult = checkCodeOff(value);
      Serial.println(checkResult);
      if(checkResult>=0){ statusToSetAtTheEnd[checkResult]=false;}
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
