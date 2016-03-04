#include "RelayController.h"

#include <Arduino.h>
template<int N>
void RelayController<N>::turnOn(short int input){
  relayChannel[input].turnOn();
}
template<int N>
void RelayController<N>::turnOff(short int input){
    relayChannel[input].turnOff();
  }
template<int N>
void RelayController<N>::initRelayController(short int tableOfPhysicalPinsForRelayInputs[]){
  for(int i= 0; i< N; ++i){
    relayChannel[i].setPhysicalPin(tableOfPhysicalPinsForRelayInputs[i]);
    relayChannel[i].initRelayPin();
  }
}
template<int N>
bool RelayController<N>::getRelayStatus(){
  bool statuses[N];
  for(int i= 0; i< N; ++i){
    statuses[i]=relayChannel[i].getStatus();
  }
  return statuses;
}
template<int N>
void RelayController<N>::setRelayToBe(int i, bool state){
  if(i > N){ return; }
  statusToBeAfterUpdate[i]=state;
}
template<int N>
void RelayController<N>::update(){
  for(int i= 0; i< N; ++i){
    if(statusToBeAfterUpdate[i]){ turnOn(i); }
    else{ turnOff(i); }
  }
}

