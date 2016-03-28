from sh import kodi_cli as kodi
import simplejson as json
import requests

class KodiTalker:
    def __init__(self):
        self._url= 'http://nest:8090'
        self._auth= (b'kodi', b'kodi')
        self._playerId= 1

    def Stop(self):
        return kodi('-s').splitlines()

    def PlayPause(self):
        return kodi('-p').splitlines()

    def PlayYoutube(self, videoId):
        with open('.videos_list', 'a') as f:
            f.write(videoId + "\n")
        return kodi('-y',videoId).splitlines()

    def getLastPlayed(self):
        lastPlayed= tuple(open(".videos_list", "r"))
        return {'lastPlayed': lastPlayed}

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
