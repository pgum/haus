/*
 Usage: ./send <unitCode> <command>
 Command is 0 for OFF and 1 for ON
 */

#include "RCSwitch.h"
#include <stdlib.h>
#include <stdio.h>

int main(int argc, char *argv[]) {
  int PIN = 7;
  char* systemCode = (char *)"10001";
  int unitCode = atoi(argv[1]);
  int command  = atoi(argv[2]);
  if (wiringPiSetup () == -1) return 1;
  RCSwitch mySwitch = RCSwitch();
  mySwitch.enableTransmit(PIN);
  switch(command) {
    case 1:
      mySwitch.switchOn(systemCode, unitCode);
      break;
    case 0:
      mySwitch.switchOff(systemCode, unitCode);
      break;
    default:
      return -1;
  }
  return 0;
}
