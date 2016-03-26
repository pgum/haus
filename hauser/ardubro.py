#from nfr24 import NRF24
import time

class Ardubro():
    def __init__(self, Aaddress="ardu1", Raddress="rasp1", relays= [0,1]):
        self._arduinoAddress= Aaddress
        self._raspberryAddress= Raddress
        self._relays= [True for relay in range(len(relays))]
        #self.radio = NRF24()

    def switchOn(self, relay):
        return self._switchRelay(relay, True)

    def switchOff(self, relay):
        return self._switchRelay(relay, False)

    def switchToggle(self, relay):
        return self._switchRelay(relay, not self._relays[relay])

    def _switchRelay(self, relay, state):
        self._sendCommand('')
        self.relays[relay]= state
        return (relay, state)

    def _sendCommand(self, command):
        pass

