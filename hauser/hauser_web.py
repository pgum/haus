from bottle import route, run, debug, template, view, static_file
from hauser import Hauser

haus = Hauser()

@route('/static/<filename>')
def server_static(filename):
  return static_file(filename, root='./static/')
@route('/static/images/<filename>')
def server_static(filename):
  return static_file(filename, root='./static/images/')

@route('/')
@view('main.tpl')
def main_page():
    pass

@route('/<device>/<action>')
def deviceActionRequest(device, action):
    result, message = haus.requestActionOnDevice(device, action)
    return {'result': result, 'message': message, 'params': {'device': device, 'action': action}}

@route('/<device>/<action>/<opcode>')
def deviceActionRequest(device, action, opcode):
    result, message = haus.requestActionOnDevice(device, action, opcode)
    return {'result': result, 'message': message, 'params': {'device': device, 'action': action, 'opcode': opcode}}

debug(True)
run(host='0.0.0.0', port=80, reloader=True)
