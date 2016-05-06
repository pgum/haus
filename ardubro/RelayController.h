#ifndef RelayController_ONCE
#define RelayController_ONCE
#include "LogicalPin.h"
typedef short channel;
typedef short nunberOfChannels;
typedef bool state;

template<nunberOfChannels N> class RelayController{
  LogicalPins<N> relays;
  state relaysNextStates[N];
public:
  void init(channel tableOfPhysicalPinsForRelayInputs[]){
    relays.initPins(tableOfPhysicalPinsForRelayInputs);
  }
  void makeOn(channel id){
    relaysNextStates[id]= true;
  }
  void makeOff(channel id){
    relaysNextStates[id]= false;
  }
  void updateRelays(){
    for(channel i= 0; i< N; ++i)
      if(relaysNextStates[i]) relays[i].turnOn();
      else relays[i].turnOff();
  }
  const bool* getStatus(){
    return relays.getStatus();
  }
};
#endif
