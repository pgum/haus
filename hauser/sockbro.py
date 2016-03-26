from sh import rpiRFsend as rfSend

class Sockbro:
    def __init__(self):
        self._sockets= {#'SocketName': {'channel':9, 'state': False}
                      }
    def switchOn(self, name):
        self._sockets[name]['state']= True;
        rfSend(self._sockets[name]['channel'], 1)
        return {'text':"Turned on socket %s" % (name), 'socket': name, 'result': True}
        print("Turned on socket %s" % (name))

    def switchOff(self, name):
        self._sockets[name]['state']= False;
        rfSend(self._sockets[name]['channel'], 0)
        return {'text':"Turned off socket %s" % (name), 'socket': name, 'result': False}
        print("Turned off socket %s" % (name))

    def switchToggle(self, name):
        print("Toggled socket %s" % name)
        if self._sockets[name]['state']: return self.switchOff(name)
        else: return self.switchOn(name)

    def getStatus(self):
        return self._sockets
