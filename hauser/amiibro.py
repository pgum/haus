import simplejson as json
import urllib, urllib2, base64
class KodiTalker:
    def prepare_json(self, method, params):
        return {'jsonrpc': '2.0',
                'method' : method,
                'params' : params,
                'id'     : 1}
     

class Amiibro:

    def broforce(self, hex=None):
        credentials = b'kodi:kodi'
        encoded_credentials = base64.b64encode(credentials)
        authorization = b'Basic ' + encoded_credentials
        headers = { 'Content-Type': 'application/json', 'Authorization': authorization }

        next_values = {'jsonrpc': '2.0',
                  'method' : 'Player.GoTo',
                  'params' : { 'playerid': 1, 
                               'to': 'next'},
                  'id'     : 1}
        prev_values = {'jsonrpc': '2.0',
                  'method' : 'Player.GoTo',
                  'params' : { 'playerid': 1, 
                               'to': 'previous'},
                  'id'     : 1}
        vol_up = { "jsonrpc": "2.0", "method": "Application.SetVolume", "params": { "volume": "increment" }, "id": 1 }
        vol_down = { "jsonrpc": "2.0", "method": "Application.SetVolume", "params": { "volume": "decrement" }, "id": 1 }
        values = {'jsonrpc': '2.0',
                  'method' : 'Player.PlayPause',
                  'params' : { 'playerid': 1},
                  'id'     : 1}
        send_song_values = { "jsonrpc":"2.0",
                             "id":"1",
                             "method":"Player.Open",
                             "params":{
                                  "item":{
                                      "file":"plugin://plugin.video.youtube/?action=play_video&videoid=iNEIpa5fpYg"}}}

        json_data = json.dumps(values)
        post_data = json_data.encode('utf-8')

        json_data1= json.dumps(send_song_values)
        post_data1 = json_data1.encode('utf-8')

        json_data3= json.dumps(vol_up)
        post_datan = json_data3.encode('utf-8')

        json_data2= json.dumps(vol_down)
        post_datap = json_data2.encode('utf-8')


        url = "http://nest:8090/jsonrpc"
        reti = hex
        req = 0
        step=10
        if(hex == "04625FAA554980"):
            req = urllib2.Request(url, post_data, headers)
            result = urllib2.urlopen(req)
            print("Play/Pause Mewtwo!")
            reti = "Mewtwo"
        if(hex == "0457ABE29A3D80"):
            req = urllib2.Request(url, post_datan, headers)
            for i in range(0, step): result = urllib2.urlopen(req)
            print("Up Pikachu")
            reti = "Pikachu"
        if(hex == "040C9A0AFE3D81"):
            print("Down Kirby")
            req = urllib2.Request(url, post_datap, headers)
            for i in range(0, step): result = urllib2.urlopen(req)
            reti = "Kirby"
        if(req != 0):
            print(result.read())
        return dict(msg=reti)

