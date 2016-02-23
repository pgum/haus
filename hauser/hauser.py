from bottle import route, run, debug, template, view, static_file
import simplejson as json
import amiibro
import ardubro

responses=[]
arduino= ardubro.Ardubro()
amiibo= amiibro.Amiibro()

def addToResponses(text):
    global responses
    responses.append(text)
    if len(responses) > 10:
        responses=responses[-10:]

@route('/')
@view('main.tpl')
def status():
    return dict(status=json.dumps(arduino.getStatus()), msg = "", responses= responses)

@route('/<device>/<action>/<channel:int>')
@view('main.tpl')
def main(device=None, action=None, channel=None):
    command="nic"
    if device and action:
        command="%s%s%s;" % (device[0], action[1], channel)
        response = arduino.sendCommand(command)
        addToResponses(response)
        status=arduino.getStatus()
    return dict(status=json.dumps(status),msg = command, responses = responses)

@route('/amigo/<hex>')
def amiibo_ctrl(hex=None):
    msgs="None Hex Amigo"
    if hex: msgs= amiibo.handleTag(hex)
    addToResponses(msgs)
    return dict(msg = msgs)

@route('/static/<filename>')
def server_static(filename):
  return static_file(filename, root='./static/')

debug(True)
run(host='0.0.0.0', port=80, reloader=True)
