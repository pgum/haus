
#include <SPI.h>
#include <RF24.h>
#include "RelayController.h"

/*
template<int N>
String RelayController::convertedStatusToString(){
  bool s = getStatus();
  for(int i= 0; i< N; ++i){
    if(status[i]){ reti += "n"; }
    else{ reti+= "f"; }
  }

*/
RelayController<2> relay;
int lightSwitchPin = 11;
bool lightSwitchState=false;

RF24 radio(3,2);
byte arduino_address[] = {"ardu1"};
byte rpi_address[] = {"RpiC"};
short relayChannelsPins[] = {8,7};
void setup(){
  
  relay.initRelayController(relayChannelsPins);
  Serial.begin(9600);
  pinMode(lightSwitchPin, INPUT_PULLUP);
  lightSwitchState= digitalRead(lightSwitchPin);

  radio.begin();
  radio.setPALevel(RF24_PA_LOW); //potem do wywalenia jak beda daleko od siebie
  radio.openWritingPipe(arduino_address);
  radio.openReadingPipe(0, rpi_address);

  radio.startListening();
}

void loop() {
  char receivedCommandBuffor[5];
  if(radio.available()){
    while(radio.available()){
      radio.read( receivedCommandBuffor, sizeof(receivedCommandBuffor));
    }
  if(receivedCommandBuffor[0] == 'r'){
    int channel= (int)receivedCommandBuffor[1] - 48;
    bool toState= receivedCommandBuffor[2] == 'n' ? true : false;
    relay.setRelayToBe(channel, toState);
  }
  bool lastState= lightSwitchState;
  lightSwitchState= digitalRead(lightSwitchPin);
  if(lastState != lightSwitchState){
    relay.setRelayToBe(0,lightSwitchState);
  }
  relay.update();
}
}
