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

@route('/devices')
def get_devices():
    available_devices={}
    for dev in haus._devices:
        available_devices[dev]=[x for x in dir(haus._devices[dev]) if not x.startswith('_')]
    return {'device_list': available_devices}

@route('/budzik/<vid>')
def playMusic(vid=None):
    haus.budzik(vid)

@route('/<device>/<action>')
@route('/<device>/<action>/<args>')
def deviceActionRequest(device, action, *args):
    return haus.requestActionOnDevice(device, action, *args)

debug(True)
run(host='0.0.0.0', port=80, reloader=True)
