import simplejson as json
import urllib, urllib2, base64
class KodiTalker:
    def __init__(self):
        self.url = "http://nest:8090/jsonrpc"
        self.playerId=1
        self.header=self.prepare_credentials("kodi:kodi")

    def prepare_credentials(self,credentials):
        encoded_credentials = base64.b64encode(self.credentials)
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
        req = urllib2.Request(self.url, command, self.headers)
        for i in range(times): results.append(urllib2.urlopen(req))
        print(results)
        return results

    def PlayPause(self):
        jsonToSend= self.prepare_json('Player.PlayPause', { 'playerid': self.playerId})
        return append(send_command(jsonToSend), times)

    def SongSkip(self, prev_or_next, times = 1):
        jsonToSend= self.prepare_json('Player.GoTo', { 'playerid': self.playerId, 'to': prev_or_next})
        return append(send_command(jsonToSend), times)

    def SongNext(self):
        return self.SongSkip("next")

    def SongPrev(self):
        return self.SongSkip("prev")

    def Volume(self,amount, increment_or_decrement):
        jsonToSend= self.prepare_json("Application.SetVolume", { "volume": increment_or_decrement })
        return send_command(jsonToSend,amount)

    def VolumeUp(amount):
        return self.Volume(amount,"increment")

    def VolumeDown(amount):
        return self.Volume(amount,"decrement")

    def PlayYoutubeSong(videoId):
        jsonToSend= self.prepare_json("Player.Open", { "item":{ "file": "plugin://plugin.video.youtube/?action=play_video&videoid=" + str(videoId)}})
        return send_command(jsonToSend)

class Amiibro:
    def __init__(self):
        self.kodiTalker = KodiTalker()
        self.amiibos={
                "04625FAA554980": self.kodiTalker.PlayPause(),
                "0457ABE29A3D80": self.kodiTalker.VolumeUp(10),
                "040C9A0AFE3D81": self.kodiTalker.VolumeDown(10)}

    def broforce(self, hex=None):
        if hex in self.amiibos:
            return dict(msg= self.amiibos[hex]())

