from bottle import route, run, debug, request, template, view
import sh

def sendToArduino(command):
    sh.sleep(1)
    sh.echo(command, _out="/dev/ttyACM0")

@route('/')
@view('main.tpl')
def main_view():
    return dict(msg= "")

@route('/<device>/<channel:int>', method='GET')
@view('main.tpl')
def device_sender(device, channel):
    action= request.GET.get('action','').strip()
    command="%s%s%s;" % (device[0], action, channel)
    sendToArduino(command)
    return dict(msg = command)

debug(True)
run(host='0.0.0.0', port=80, reloader=True)
