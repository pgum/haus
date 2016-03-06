from sh import rpiRFsend as rfSend

class Sockbro:
    def __init__(self):
        self.sockets= {2: {'name': 'ladowarka w sypialni', 'channel':2, 'state': False},
                       4: {'name': 'Reflektor w salonie', 'channel':4, 'state': False},
                       5: {'name': 'Lampka w magazynie', 'channel':5, 'state': False}}

    def switchOn(self, channel):
        self.sockets[channel]['state']=True;
        rfSend(self.sockets[channel]['channel'], 1)

    def switchOff(self, channel):
        self.sockets[channel]['state']=False;
        rfSend(self.sockets[channel]['channel'], 0)
