from bottle import route, run, debug, template, view, static_file
from ardubro import Ardubro
from amiibro import Amiibro
from koditalker import KodiTalker

responses=[]
arduino= Ardubro()
amiibo= Amiibro()
kodiTalker = KodiTalker()
amiibo.amiibos={
                "04625FAA554980": {'name': "Mewtwo" , 'method': kodiTalker.PlayPause , 'params': None},
                "0457ABE29A3D80": {'name': "Pikachu", 'method': kodiTalker.VolumeUp  , 'params': 20},
                "040C9A0AFE3D81": {'name': "Kirby"  , 'method': kodiTalker.VolumeDown, 'params': 20}}

def addToResponses(text):
    global responses
    responses.append(text)
    if len(responses) > 10:
        responses=responses[-10:]

@route('/')
@view('main.tpl')
def status():
    return dict(msg = "", responses= responses)

@route('/kodi/<action>/<param>')
@route('/light/<action>/<channel:int>')
def blank(*args, **kwargs):
    return kwargs

@route('/relay/<action>/<channel:int>')
@view('main.tpl')
def main(action=None, channel=None):
    response=None
    if action == "on":  response = arduino.switchRelayOn(channel)
    if action == "off": response = arduino.switchRelayOff(channel)
    if response: addToResponses(response)
    return dict(msg = "Relay action: Turn %s %s; Response: %s" % (channel, action, response), responses = responses)

@route('/amigo/<tag>')
def amiibo_ctrl(tag=None):
    msgs="None Hex Amigo"
    if tag: msgs= amiibo.handleTag(tag)
    addToResponses(msgs)
    return dict(msg = msgs)

@route('/static/<filename>')
def server_static(filename):
  return static_file(filename, root='./static/')

debug(True)
run(host='0.0.0.0', port=8070, reloader=True)
