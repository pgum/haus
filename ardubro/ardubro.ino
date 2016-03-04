#include <SPI.h>
#include <RF24.h>
#include <RelayController.h>

using MyRelay= RelayController<2>;
MyRelay rc;
RF24 radio(3,2)
int lightSwitchPin = 11;
bool lightSwitchState=false;

void setup(){
  int relayChannelsPins[] = {8,7}
  rc.initRelayController(relayChannelPins);
  Serial.begin(9600);
  pinMode(lightSwitchPin, INPUT_PULLUP);
  lightSwitchState= digitalRead(lightSwitchPin);
}

void loop() {
  bool lastState= lightSwitchState;
  lightSwitchState= digitalRead(lightSwitchPin);
  if(lastState != lightSwitchState){
    rc.setRelayToBe(0,lightSwitchState);
  }
  rc.update();
}
