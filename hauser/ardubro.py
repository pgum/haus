from serial import Serial, SerialException
from time import sleep


class Ardubro(Serial):
    def __init__(self, relays= 2, setDebug=True, port='/dev/ttyACM0', baudrate=9600, *args, **kwargs):
        self.established=False
        self.debug= setDebug
        self.relayStatus= [True for relay in range(relays)]
        self.established=False
        try:
            #Serial.__init__(self, port=port, baudrate=baudrate, *args, **kwargs)
            #self.established=True
            pass
        except SerialException:
            pass

    def switchOn(self, relay):
        self.switchRelay(relay,True,"On")

    def switchOff(self, relay):
        self.switchRelay(relay,False,"Off")

    def switchRelay(self, relay, state, On_or_Off):
        print("switchRelay: %s, to state %s" % (relay, On_or_Off))
        if not self.established: return
        self.relayStatus[relay]=state
        self.sendCommand("r%s%s;" %(On_or_Off[-1], relay))

    def sendCommand(self, command):
        if self.debug: print("Ardubro: sending: %s" % command)
        sleep(0.3)
        self.write(command)
        out=""
        while self.inWaiting() > 0:
            out = self.read(1)
        if self.debug: print("Ardubro: recieved: %s" % out)
        return out
