#include "RelayController.h"
/*#include <SPI.h>
#include <RF24.h>
RF24 radio(3,2);*/
/*void initRadio(){
  byte arduino_address[]= {"ardu1"};
  byte rpi_address[]= {"RpiC"};
  radio.begin();
  radio.setPALevel(RF24_PA_LOW); //potem do wywalenia jak beda daleko od siebie
  radio.openWritingPipe(arduino_address);
  radio.openReadingPipe(0, rpi_address);
  radio.startListening();
}*/
/*void handleRadio(){
  char receivedCommandBuffor[5];
  if(radio.available()){
    while(radio.available())
      radio.read(receivedCommandBuffor, sizeof(receivedCommandBuffor));
    if(receivedCommandBuffor[0] == 'r'){
      int channel= (int)receivedCommandBuffor[1] - 48;
      bool isToBeOn= receivedCommandBuffor[2] == 'n';
      if(isToBeOn) relay.makeOn(channel);
      else relay.makeOff(channel);
    }
  }
}*/
/*String convertedStatusToString(bool statusArray[], short num){
  String reti;
  for(short i= 0; i< num; ++i)
    if(statusArray[i]) reti += "n";
    else reti+= "f";
  return reti;
}*/

const int lightSwitchPin = 11;
const short relayChannelsPins[]= {8,7};

RelayController<2> relay;
bool lightSwitchState=false;

void setup(){

  relay.init(relayChannelsPins);
  pinMode(lightSwitchPin, INPUT_PULLUP);
  lightSwitchState= digitalRead(lightSwitchPin);
  //initRadio();
}

void loop(){
  //handleRadio();
  bool lastState= lightSwitchState;
  lightSwitchState= digitalRead(lightSwitchPin);
  if(lastState != lightSwitchState && lightSwitchState)
    relay.makeOn(0);
  else
    relay.makeOff(0);
  relay.update();
}
