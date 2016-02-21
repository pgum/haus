from bottle import route, run, debug, template, view, static_file
import amiibro
import ardubro

responses=[]
arduino= ardubro.Ardubro()
amiibo= amiibro.Amiibro()

@route('/')
@route('/<device>/<action>/<channel:int>')
@view('main.tpl')
def main(device=None, action=None, channel=None):
    command="nic"
    if device and action:
        command="%s%s%s;" % (device[0], action[1], channel)
        responses.append(arduino.sendCommand(command))
    status=arduino.getStatus()
    return dict(status=json.dumps(status),msg = command, responses = responses)

@route('/resetresp')
def resetresponses():
    responses=[]
    return dict()


@route('/amigo/<hex>')
def amiibo_ctrl(hex=None):
    msgs= amiibo.broforce(hex)
    responses.append(msgs)
    return dict(msg = msgs)


@route('/static/<filename>')
def server_static(filename):
  return static_file(filename, root='./static/')

debug(True)
run(host='0.0.0.0', port=80, reloader=True)
