#include "LogicalPin.h"
#include <Arduino.h>

void LogicalPin::setPhysicalPin(int physicalPin){
  pin = physicalPin;
  low = LOW;
  high= HIGH;
}
bool LogicalPin::turnOn(){
  pinStatus=true;
  digitalWrite(pin, low);
  return pinStatus;
}
bool LogicalPin::turnOff(){
  pinStatus=false;
  digitalWrite(pin, high);
  return pinStatus;
}
bool LogicalPin::toggle(){
  if(pinStatus) turnOff();
  else turnOn();
  return pinStatus;
}
void LogicalPin::initRelayPin(){
  pinMode(pin, OUTPUT);
  turnOff();
}
bool LogicalPin::getStatus(){
  return pinStatus;
}

