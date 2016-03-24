from bottle import route, run, debug, template, view, static_file
from hauser import Hauser

haus = Hauser()

@route('/static/<filename>')
def server_static(filename):
  return static_file(filename, root='./static/')

@route('/')
@view('main.tpl')
def main_page():
    pass

@route('/devices/')
def get_devices():
    available_devices=[]
    for dev in haus.devices:
        available_devices.append(dev)
    return {'device_list': available_devices}

@route('/budzik/<vid>')
def playMusic(vid=None):
    haus.budzik(vid)

@route('/<device>/<action>')
@route('/<device>/<action>/<channel>')
def deviceActionRequest(device=None, action=None, channel=None):
    return haus.requestActionOnDevice(device, action, channel)


debug(True)
run(host='0.0.0.0', port=80, reloader=True)
