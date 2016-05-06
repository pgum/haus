#ifndef LogicalPin_ONCE
#define LogicalPin_ONCE
#include <Arduino.h>

typedef short channel;
typedef short nunberOfChannels;
typedef bool state;

class LogicalPin{
  channel pin;
  state s;
public:
  LogicalPin(): pin(-1), s(false){}
  LogicalPin(short physicalPin): pin(physicalPin), s(false){}
  void initPin(short physicalPin){
    pin= physicalPin;
    pinMode(pin, OUTPUT);
  }
  void turnOn(){
    s=true;
    digitalWrite(pin, LOW);
  }
  void turnOff(){
    s=false;
    digitalWrite(pin, HIGH);
  }
  void toggle(){
    if(s) turnOff();
    else turnOn();
  }
  const bool getState(){
      return s;
  }
};

template <nunberOfChannels N> class LogicalPins{
    LogicalPin pinData[N];
    state pinStatus[N], isInitialized;
public:
  LogicalPins() : pinData(), isInitialized(false){}
  LogicalPin &operator[](channel index){
    return pinData[index];
  }
  void initPins(channel tableOfPhysicalPinsForRelayInputs[]){
    for(channel i= 0; i< N; ++i) 
      pinData[i].initPin(tableOfPhysicalPinsForRelayInputs[i]);
    isInitialized= true;
  }
  state* getStatus(){
    for(channel i= 0; i< N; ++i)
      pinStatus[i]= pinData[i].getState();
    return pinStatus;
  }
};
#endif
