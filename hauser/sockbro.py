from sh import rpiRFsend as rfSend

class Sockbro:
    def __init__(self):
        self.sockets= {#'SocketName': {'channel':9, 'state': False}
                      }
    def switchOn(self, name):
        self.sockets[name]['state']= True;
        rfSend(self.sockets[name]['channel'], 1)
        print("Turned on socket %s" % (name))

    def switchOff(self, name):
        self.sockets[name]['state']= False;
        rfSend(self.sockets[name]['channel'], 0)
        print("Turned off socket %s" % (name))

    def switchToggle(self, name):
        if self.sockets[name]['state']: self.switchOff(name)
        else: self.switchOn(name)
        print("Toggled socket %s to %s" % (name, self.sockets[name]['state']))

    def getStatus(self):
        return self.sockets
