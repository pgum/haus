from sh import rpiRFsend as rfSend

class Sockbro:
    def __init__(self):
        self.sockets= {2: {'name': 'ladowarka w sypialni', 'channel':2, 'state': False},
                       4: {'name': 'Reflektor w salonie', 'channel':4, 'state': False},
                       5: {'name': 'Lampka w magazynie', 'channel':5, 'state': False}}

    def switchOn(self, channel):
        self.sockets[channel]['state']=True;
        print("LIGHT switchOn %s" % (channel) )
        rfSend(self.sockets[channel]['channel'], 1)

    def switchOff(self, channel):
        self.sockets[channel]['state']=False;
        print("LIGHT switchOff %s" % (channel) )
        rfSend(self.sockets[channel]['channel'], 0)

    def switchToggle(self, channel):
        print("LIGHT switchToggle %s" % (channel) )
        if self.sockets[channel]['state']: self.switchOff(channel)
        else: self.switchOn(channel)
