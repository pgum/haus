#include "LogicalPin.h"

template<int N>
class RelayController{
  LogicalPin relayChannel[N];
  bool statusToBeAfterUpdate[N];
public:
  RelayController(){}

  void turnOn(short int input);
  void turnOff(short int input);
  void initRelayController(short int tableOfPhysicalPinsForRelayInputs[]);
  bool getRelayStatus();
  void setRelayToBe(int i, bool state);
  void update();
};

