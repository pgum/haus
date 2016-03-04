class RelayPin{
  bool status;
  int pin;
public:
  RelayPin(): status(false), pin(-1){}
  void setPhysicalPin(int physicalPin);
  void initRelayPin();
  bool turnOn();
  bool turnOff();
  bool toggle();
  bool getStatus();
};

template<int N>
class RelayController{
  RelayPin relayChannel[N];
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

