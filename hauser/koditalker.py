import simplejson as json
import urllib, base64
try : import urllib2
except: import urllib.request

class KodiTalker:
    def __init__(self):
        self.url = "http://nest:8090/jsonrpc"
        self.playerId=1
        self.header=self.prepare_credentials(b"kodi:kodi")

    def prepare_credentials(self,credentials):
        encoded_credentials = base64.b64encode(credentials)
        authorization = b'Basic ' + encoded_credentials
        return { 'Content-Type': 'application/json', 'Authorization': authorization }

    def prepare_json(self, method, params):
        message= {'jsonrpc': '2.0',
                  'method' : method,
                  'params' : params,
                  'id'     : self.playerId}
        return self.encode_command(message)

    def encode_command(self, preparedJson):
        json_data = json.dumps(preparedJson)
        post_data = json_data.encode('utf-8')
        return post_data

    def send_command(self,command, times=1):
        results=[]
        req = urllib2.Request(self.url, command, self.header)
        for i in range(times): results.append(urllib2.urlopen(req))
        print(results)
        return results

    def PlayPause(self):
        jsonToSend= self.prepare_json('Player.PlayPause', { 'playerid': self.playerId})
        return self.send_command(jsonToSend)

    def SongSkip(self, prev_or_next, times = 1):
        jsonToSend= self.prepare_json('Player.GoTo', { 'playerid': self.playerId, 'to': prev_or_next})
        return self.send_command(jsonToSend, times)

    def SongNext(self):
        return self.SongSkip("next")

    def SongPrev(self):
        return self.SongSkip("prev")

    def Volume(self,amount, increment_or_decrement):
        jsonToSend= self.prepare_json("Application.SetVolume", { "volume": increment_or_decrement })
        return self.send_command(jsonToSend, amount)

    def VolumeUp(self, amount):
        return self.Volume(amount,"increment")

    def VolumeDown(self, amount):
        return self.Volume(amount,"decrement")

    def PlayYoutubeSong(self, videoId):
        jsonToSend= self.prepare_json("Player.Open",
                { "item": { "file": "plugin://plugin.video.youtube/?action=play_video&videoid=" + str(videoId)}})
        return self.send_command(jsonToSend)

import requests
class KodiTalker2:
    def __init__(self):
        self.url = "http://nest:8090/jsonrpc"
        self.playerId=1
        self.auth=(b"kodi",b"kodi")

    def prepare_json(self, method, params):
        return {'jsonrpc': '2.0',
                'method' : method,
                'params' : params,
                'id'     : self.playerId}

    def send_command(self,command, times=1):
        req = requests.get(self.url, params= {'request': command}, auth=self.auth)
        print(req.text)
        return req.text

    def PlayPause(self):
        jsonToSend= self.prepare_json('Player.PlayPause', { 'playerid': self.playerId})
        self.send_command(jsonToSend)

    def SongSkip(self, prev_or_next, times = 1):
        jsonToSend= self.prepare_json('Player.GoTo', { 'playerid': self.playerId, 'to': prev_or_next})
        self.send_command(jsonToSend, times)

    def SongNext(self):
        self.SongSkip("next")

    def SongPrev(self):
        self.SongSkip("prev")

    def Volume(self,amount, increment_or_decrement):
        jsonToSend= self.prepare_json("Application.SetVolume", { "volume": increment_or_decrement })
        for i in range(times):
            self.send_command(jsonToSend, amount)

    def VolumeUp(self, amount):
        self.Volume(amount,"increment")

    def VolumeDown(self, amount):
        self.Volume(amount,"decrement")

    def PlayYoutubeSong(self, videoId):
        jsonToSend= self.prepare_json("Player.Open",
                { "item": { "file": "plugin://plugin.video.youtube/?action=play_video&videoid=" + str(videoId)}})
        return self.send_command(jsonToSend)
