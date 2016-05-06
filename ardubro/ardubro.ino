#include "RelayController.h"
#include <SPI.h>
//#include <RF24.h>

String convertedStatusToString(bool statusArray[], short num){
  String reti;
  for(int i= 0; i< num; ++i)
    if(statusArray[i]) reti += "n";
    else reti+= "f";
  return reti;
}

RelayController<2> relay;
int lightSwitchPin = 11;
bool lightSwitchState=false;

//RF24 radio(3,2);
byte arduino_address[]= {"ardu1"};
byte rpi_address[]= {"RpiC"};
short relayChannelsPins[]= {8,7};
/*
void initRadio(){
  radio.begin();
  radio.setPALevel(RF24_PA_LOW); //potem do wywalenia jak beda daleko od siebie
  radio.openWritingPipe(arduino_address);
  radio.openReadingPipe(0, rpi_address);
  radio.startListening();
}*/
void setup(){
  relay.initRelayController(relayChannelsPins);
  Serial.begin(9600);
  pinMode(lightSwitchPin, INPUT_PULLUP);
  lightSwitchState= digitalRead(lightSwitchPin);

  //initRadio();
}
/*void handleRadio(){
  char receivedCommandBuffor[5];
  if(radio.available()){
    while(radio.available())
      radio.read(receivedCommandBuffor, sizeof(receivedCommandBuffor));
    if(receivedCommandBuffor[0] == 'r'){
      int channel= (int)receivedCommandBuffor[1] - 48;
      bool toState= receivedCommandBuffor[2] == 'n';
      relay.setState(channel, toState);
    }
  }
}*/
void loop() {
  //handleRadio();
  bool lastState= lightSwitchState;
  lightSwitchState= digitalRead(lightSwitchPin);
  if(lastState != lightSwitchState && lightSwitchState)
    relay.makeOn(0);
  else
    relay.makeOff(0);
  relay.update();
}

