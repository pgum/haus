from serial import Serial, SerialException
from time import sleep


class Ardubro(Serial):
    def __init__(self, relays= 2, setDebug=True, port='/dev/ttyACM0', baudrate=9600, *args, **kwargs):
        self.established=False
        self.debug= setDebug
        self.port= port
        self.baudrate= baudrate
        self.relayStatus= [True for relay in range(relays)]

    def initConnection(self):
        self.established=False
        if not self.established:
            try:
                Serial.__init__(self, port=self.port, baudrate=self.baudrate, *args, **kwargs)
                self.established=True
            except SerialException:
                pass
        return self.established

    def switchRelayOn(self, relay):
        self.relayStatus[relay]=True
        self.sendCommand("rn%s;" % relay)

    def switchRelayOff(self, relay):
        self.relayStatus[relay]=False
        self.sendCommand("rf%s;" % relay)

    def sendCommand(self, command):
        if self.debug: print("Ardubro: sending: %s" % command)
        sleep(0.3)
        self.write(command)
        out=""
        while self.inWaiting() > 0:
            out = self.read(1)
        if self.debug: print("Ardubro: recieved: %s" % out)
        return out

    def getStatus(self):
        status = "ffnnnn" #sendCommand("s;")
        return {'light': (status[0], status[1], status[2]), 'relay': (status[4], status[5])}

