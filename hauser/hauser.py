from ardubro import Ardubro
from amiibro import Amiibro
from sockbro import Sockbro

class Hauser:
    def __init__(self):
        self.responses=[]
        self.devices={
                'relays' : Ardubro(),
                'amiibo' : Amiibro(),
                'sockets': Sockbro()
                }

    def status(self):
        return dict(msg = "", responses= self.responses)

    def requestActionOnDevice(self, device, action, channel):
        if device in self.devices:
            result= getattr(self.devices[device], action)(channel)
            return result

    def amiiboControl(self, tag=None):
        if tag: response= self.devices['amiibo'].handleTag(tag)
        self.responses.append(response)
