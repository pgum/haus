from ardubro import Ardubro
from amiibro import Amiibro
from sockbro import Sockbro
from koditalker import KodiTalker
from sys import exc_info as exceptionDetails

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

    def requestActionOnDevice(self, device, action, *args):
        try:
            return ('ok', getattr(self._devices[device], action)(*args))
        except:
            return ('error', str(exceptionDetails()[1]))

    def getAvailableCommands(self):
        available_commands={}
        for dev in self._devices:
            available_commands[dev]=[x for x in dir(self._devices[dev]) if not x.startswith('_')]
        return available_commands
