from sh import rpiRFsend as rfSend

class Sockbro:
    def __init__(self):
        self.sockets= {
                       'Nieuzywane': {'channel':5, 'state': False},
                       'Lampka': {'channel': 2, 'state': False},
                       'Salon': {'channel': 4, 'state': False}}

    def switchOn(self, name):
        self.sockets[name]['state']=True;
        print("Turned on socket %s" % (name) )
        rfSend(self.sockets[name]['channel'], 1)

    def switchOff(self, name):
        self.sockets[name]['state']=False;
        print("Turned off socket %s" % (name) )
        rfSend(self.sockets[name]['channel'], 0)

    def switchToggle(self, name):
        if self.sockets[channel]['state']: self.switchOff(channel)
        else: self.switchOn(channel)
        print("Toggled socket %s to %s" % (name, self.sockets[name]['state']))
