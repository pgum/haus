class LogicalPin{
  short pin;
  bool pinStatus;
  bool low, high;
  
public:
  LogicalPin(): pinStatus(false), pin(-1){}
  void setPhysicalPin(int physicalPin);
  void initRelayPin();
  bool turnOn();
  bool turnOff();
  bool toggle();
  bool getStatus();
};

