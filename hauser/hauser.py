from ardubro import Ardubro
from amiibro import Amiibro
from sockbro import Sockbro
from koditalker import KodiTalker

class Hauser:
    def __init__(self):
        self._devices={
                'relays' : Ardubro(),
                'amiibo' : Amiibro(),
                'sockets': Sockbro(),
                'kodi'   : KodiTalker(),
                'self'   : self}
        self._devices['amiibo']._amiibos={
                #'043BAE92BF4881': {'name': 'PixelMario'  , 'method': KodiTalker().PlayPause, 'params': None},
                '04625FAA554980': {'name': 'Mewtwo', 'method': self._devices['kodi'].PlayPause, 'params': None},
                '0457ABE29A3D80': {'name': 'Pikachu', 'method': self._devices['kodi'].VolumeUp, 'params': 20},
                '040C9A0AFE3D81': {'name': 'Kirby', 'method': self._devices['kodi'].VolumeDown, 'params': 20},
                '041C9982034980': {'name': 'DuckHunt', 'method': self._devices['sockets'].switchToggle, 'params': 'Salon'},
                '049F1122704080': {'name': 'Mario', 'method': self._devices['sockets'].switchToggle, 'params': 'Nieuzywane'}}
        self._devices['sockets']._sockets={
                                       'Nieuzywane': {'channel':5, 'state': False},
                                       'Lampka': {'channel': 2, 'state': False},
                                       'Salon': {'channel': 4, 'state': False}}
    def budzik(self, videoID):
        print("budzik youtube: %s" % videoID)
        KodiTalker().PlayYoutubeSong(videoID)

    def requestActionOnDevice(self, device, action, *args):
        if device in self._devices:
            if args: return {'type':'ok', 'msg': getattr(self._devices[device], action)(*args)}
            else: return {'type':'ok', 'msg': getattr(self._devices[device], action)()}
        else:
            return {'type':'error','msg':'device %s not found' % device }

