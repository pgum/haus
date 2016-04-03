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
        return self._sendCommand("Player.Stop", {"playerid": self._playerId})

    def PlayPause(self):
        return self._sendCommand("Player.PlayPause", {"playerid": self._playerId})

    #last with kodi_cli dependency
    def PlayYoutube(self, videoId):
        return [self._yt.SaveInformationAboutVideo(videoId), kodi('-y',videoId).splitlines()]

    def getLastPlayed(self):
        return self._yt.LoadVideosInfoFromFile()

    def getVolume(self):
        return self._sendCommand("Application.GetProperties", {"properties": ["volume"]})

    def VolumeTo(self,amount):
        return self._sendCommand('Application.SetVolume', {'volume': int(amount)})

    def _sendCommand(self, method, params):
        payload= {'jsonrpc': '2.0',
                  'method' : method,
                  'params' : params,
                  'id'     : self._playerId}
        request_data= json.dumps(payload).encode()
        prepared_url= requests.Request('GET', self._url + '/jsonrpc?request=' + request_data).prepare().url
        r= requests.get(url= prepared_url, auth= self._auth)
        return {"payload": payload, "response": json.loads(r.text), "prepared url": prepared_url}
