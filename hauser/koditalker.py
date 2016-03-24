from sh import kodi_cli as kodi
import simplejson as json
import requests
class KodiTalker:
    def __init__(self):
        self.url= 'http://nest:8090'
        self.auth= (b'kodi', b'kodi')
        self.playerId= 1

    def PlayPause(self):
        kodi('-p')

    def VolumeUp(self, amount):
        self._volume(amount,'increment')

    def VolumeDown(self, amount):
        self._volume(amount,'decrement')

    def PlayYoutubeSong(self, videoId):
        kodi('-y',videoId)

    def _volume(self, amount=20, increment_or_decrement='increment'):
        for i in range(int(amount)):
            self._sendCommand('Application.SetVolume', {'volume': increment_or_decrement})

    def _prepareUrl(self, method, params):
        request_raw= {'jsonrpc': '2.0',
                     'method' : method,
                     'params' : params,
                     'id'     : self.playerId}
        request_data = json.dumps(request_raw).encode('utf-8')
        return requests.Request('GET', self.url + '/jsonrpc?request=' + request_data).prepare().url

    def _sendCommand(self, method, params):
        r= requests.get(url= self._prepareUrl(method, params), auth= self.auth)
        print(r.text)
