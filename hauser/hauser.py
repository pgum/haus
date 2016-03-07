from ardubro import Ardubro
from amiibro import Amiibro
from sockbro import Sockbro
from koditalker import KodiTalker

class Hauser:
    def __init__(self):
        self.responses=[]
        self.devices={
                'relays' : Ardubro(),
                'amiibo' : Amiibro(),
                'sockets': Sockbro()
                }
        self.devices['amiibo'].amiibos={
                "04625FAA554980": {'name': "Mewtwo" , 'method': KodiTalker().PlayPause , 'params': None},
                "0457ABE29A3D80": {'name': "Pikachu", 'method': KodiTalker().VolumeUp  , 'params': 20},
                "040C9A0AFE3D81": {'name': "Kirby"  , 'method': KodiTalker().VolumeDown, 'params': 20},
                "043BAE92BF4881": {'name': "Mario"  , 'method': self.devices['sockets'].switchOn, 'params': 4},
                "041C9982034980": {'name': "DuckHunt", 'method': self.devices['sockets'].switchOn, 'params': 4},
                }

    def requestActionOnDevice(self, device, action, channel):
        if device in self.devices:
            result= getattr(self.devices[device], action)(channel)
            return result

    def amiiboControl(self, tag=None):
        if tag: response= self.devices['amiibo'].handleTag(tag)
        self.responses.append(response)
