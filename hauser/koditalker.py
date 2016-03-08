import simplejson as json
import requests
class KodiTalker:
    def __init__(self):
        self.url= 'http://nest:8090'
        self.auth= (b'kodi', b'kodi')
        self.playerId= 1

    def PlayPause(self):
        self._sendCommand('Player.PlayPause', {'playerid': self.playerId})

    def VolumeUp(self, amount):
        self._volume(amount,'increment')

    def VolumeDown(self, amount):
        self._volume(amount,'decrement')

    def SongNext(self):
        self._songSkip('next')

    def SongPrev(self):
        self._songSkip('prev')

    def PlayYoutubeSong(self, videoId):
        self._sendCommand('Player.Open',
                {'item': {'file': 'plugin://plugin.video.youtube/?action=play_video&videoid='+ str(videoId)}})

    def _songSkip(self, prev_or_next, times = 1):
        for i in range(times):
            self._sendCommand('Player.GoTo', {'playerid': self.playerId, 'to': prev_or_next})

    def _volume(self, amount, increment_or_decrement):
        for i in range(amount):
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
