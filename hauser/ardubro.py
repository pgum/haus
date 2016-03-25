#from nfr24 import NRF24
import time

class Ardubro():
    def __init__(self, Aaddress="ardu1", Raddress="rasp1", relays= 2):
        self._arduinoAddress= Aaddress
        self._raspberryAddress= Raddress
        self._relays= [True for relay in range(relays)]
        #self.radio = NRF24()

    def switchOn(self, relay):
        self._switchRelay(relay, True)

    def switchOff(self, relay):
        self._switchRelay(relay, False)

    def switchToggle(self, relay):
        self._switchRelay(relay, not self._relays[relay])

    def _switchRelay(self, relay, state):
        self._relays[int(relay)]= state
        self._sendCommand("")

    def _sendCommand(self, command):
        pass

