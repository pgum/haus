class SocketsTalker:
    def __init__(self, homePin, *sockets):
        self.homePin= homePin
        self.sockets= {'A': {'name': 'lampka na biurku', 'channel':'10000' },
                       'B': {'name': 'ladowarka w sypialni', 'channel':'01000' },
                       'C': {'name': None, 'channel': None },
                       'D': {'name': 'Reflektor w salonie', 'channel':'00010' }}
        self.sockets_state = dict(zip(self.sockets.keys(), [False for i in range(len(self.sockets))]))
        class RCSwitch():
            def enableTransmit(self, dummy):
                pass
            def switchOn(self, dummy1, dummy2):
                pass
            def switchOff(self, dummy1, dummy2):
                pass
        self.rcSwitch= RCSwitch()
        self.rcSwitch.enableTransmit(physicalPin)

    def turnOn(self,socket):
        if socket in self.sockets:
            rcSwitch.switchOn(self.homePin, self.sockets[socket]['channel'])
            self.sockets_state[socket]=True

    def turnOff(self,socket):
        if socket in self.sockets:
            rcSwitch.switchOff(self.homePin, self.sockets[socket]['channel'])
            self.sockets_state[socket]=False


