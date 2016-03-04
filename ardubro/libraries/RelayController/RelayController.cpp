#include "RelayController.h"

void RelayPin::setPhysicalPin(int physicalPin){
  pin = physicalPin;
}
bool RelayPin::turnOn(){
  status=true;
  digitalWrite(pin, LOW);
  return status;
}
bool RelayPin::turnOff(){
  status=false;
  digitalWrite(pin, HIGH);
  return status;
}
bool RelayPin::toggle(){
  if(status){turnOff();}
  else{turnOn();}
  return status;
}
void RelayPin::initRelayPin(){
  pinMode(pin, OUTPUT);
  turnOff();
}
bool RelayPin::getStatus(){
  return status
}

template<int N>
void RelayController::turnOn(short int input){
  relayChannel[input].turnOn();
}
template<int N>
void RelayController::turnOff(short int input){
    relayChannel[input].turnOff();
  }
template<int N>
void RelayController::initRelayController(int *tableOfPhysicalPinsForRelayInputs){
  for(int i= 0; i< N; ++i){
    relayChannel[i].setPhysicalPin(tableOfPhysicalPinsForRelayInputs[i]);
    relayChannel[i].initRelayPin();
  }
}
template<int N>
String RelayController::convertedStatusToString(){
  bool s = getStatus();
  for(int i= 0; i< N; ++i){
    if(status[i]){ reti += "n"; }
    else{ reti+= "f"; }
  }
template<int N>
bool RelayController::getRelayStatus(){
  bool statuses[N];
  for(int i= 0; i< N; ++i){
    statuses[i]=relayChannel[i].getStatus();
  }
  return statuses;
}
template<int N>
void RelayController::setRelayToBe(int i, bool state){
  statusToSetAtTheEnd[i]=state;
}
template<int N>
void RelayController::update(){
  for(int i= 0; i< N; ++i){
    if(statusToSetAtTheEnd[i]){ turnOn(i); }
    else{ turnOff(i); }
  }
}

