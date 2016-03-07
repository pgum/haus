from bottle import route, run, debug, template, view, static_file
from hauser import Hauser

haus = Hauser()

def makeDict(what, channel, action):
    return dict(msg = "%s action: Turn %s %s" % (what, channel, action), responses = haus.responses)

@route('/')
@view('main.tpl')
def nop():
    return dict(msg = "~-~-~-~-~", responses= haus.responses)

@route('/<device>/<action>/<channel:int>')
@view('main.tpl')
def deviceActionRequest(device=None, action=None, channel=None):
    haus.requestActionOnDevice(device, action, channel)
    return makeDict(device, channel, action)

@route('/amigo/<tag>')
@route('/amiicode/<tag>')
def amiiboNfcTagRequest(tag=None):
    msgs="Not Hex Amigo"
    if tag: haus.devices['amiibo'].handleTag(tag)
    return dict(msg = haus.responses[-1])

@route('/static/<filename>')
def server_static(filename):
  return static_file(filename, root='./static/')

debug(True)
run(host='0.0.0.0', port=8070, reloader=True)
