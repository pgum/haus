from ardubro import Ardubro
from amiibro import Amiibro
from sockbro import Sockbro
from koditalker import KodiTalker

class Hauser:
    def __init__(self):
        self.devices={
                'relays' : Ardubro(),
                'amiibo' : Amiibro(),
                'sockets': Sockbro(),
                'kodi'   : KodiTalker(),
                'self'   : self}
        self.devices['amiibo'].amiibos={
                #'043BAE92BF4881': {'name': 'PixelMario'  , 'method': KodiTalker().PlayPause, 'params': None},
                '04625FAA554980': {'name': 'Mewtwo', 'method': self.devices['kodi'].PlayPause, 'params': None},
                '0457ABE29A3D80': {'name': 'Pikachu', 'method': self.devices['kodi'].VolumeUp, 'params': 20},
                '040C9A0AFE3D81': {'name': 'Kirby', 'method': self.devices['kodi'].VolumeDown, 'params': 20},
                '041C9982034980': {'name': 'DuckHunt', 'method': self.devices['sockets'].switchToggle, 'params': 'Salon'},
                '049F1122704080': {'name': 'Mario', 'method': self.devices['sockets'].switchToggle, 'params': 'Nieuzywane'}}

    def budzik(self, videoID):
        print("budzik youtube: %s" % videoID)
        KodiTalker().PlayYoutubeSong(videoID)

    def requestActionOnDevice(self, device, action, *args):
        if device in self.devices:
            return getattr(self.devices[device], action)(*args)
        else:
            return {'type':'error','msg':'device %s not found' % device }

