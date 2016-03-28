from bottle import route, run, debug, template, view, static_file
from hauser import Hauser
import simplejson as json

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

@route('/meta/rmLog')
def rmLog():
    with open('static/log.json','w') as f: f.write("")
    return getLog()

@route('/meta/getLog')
def getLog():
    ret="["
    with open('static/log.json', 'r') as f:
        for line in f: ret=ret+ line
    message= json.loads(ret+ "]")
    msg= {'result': 'ok', 'message': message, 'params': {'device': 'meta', 'action': 'getLog'}}
    return msg

@route('/<device>/<action>')
def deviceActionRequest(device, action):
    result, message = haus._requestActionOnDevice(device, action)
    msg= {'result': result, 'message': message, 'params': {'device': device, 'action': action}}
    return msg

@route('/<device>/<action>/<opcode>')
def deviceActionRequest(device, action, opcode):
    result, message = haus._requestActionOnDevice(device, action, opcode)
    with open('./static/log.json','a') as f:
        msg= {'result': result, 'message': message, 'params': {'device': device, 'action': action, 'opcode': opcode}}
        f.write("%s,"%json.dumps(msg))
    return msg

debug(True)
run(host='0.0.0.0', port=80, reloader=True)
