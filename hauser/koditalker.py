from sh import kodi_cli as kodi
import simplejson as json
import requests
from youtubeTalker import YoutubeTalker

class KodiTalker:
    def __init__(self):
        self._url= 'http://nest:8090'
        self._auth= (b'kodi', b'kodi')
        self._playerId= 1
        self._yt=YoutubeTalker()

    def Stop(self):
        return kodi('-s').splitlines()

    def PlayPause(self):
        return kodi('-p').splitlines()

    def PlayYoutube(self, videoId):
        ytResult= self._yt.SaveInformationAboutVideo(videoId)
        return {'KodiTalker': kodi('-y',videoId).splitlines(), 'YoutubeTalker': ytResult}

    def getLastPlayed(self):
        return self._yt.LoadVideosInfoFromFile()

    def VolumeUp(self, amount=20):
        return self._volume(amount,'increment')

    def VolumeDown(self, amount=20):
        return self._volume(amount,'decrement')

    def _volume(self, amount, direction):
        for i in range(amount):
            last= self._sendCommand('Application.SetVolume', {'volume': direction})
        return last
    def VolumeTo(self,amount):
        return self._sendCommand('Application.SetVolume', {'volume': int(amount)})
    def _sendCommand(self, method, params):
        request_raw= {'jsonrpc': '2.0',
                     'method' : method,
                     'params' : params,
                     'id'     : self._playerId}
        request_data = json.dumps(request_raw).encode('utf-8')
        prepared_url= requests.Request('GET', self._url + '/jsonrpc?request=' + request_data).prepare().url
        r= requests.get(url= prepared_url, auth= self._auth)
        print(r.text)
        return {"request_raw": request_raw, "response": r.text}
