from bottle import route, run, debug, template, view, static_file
import simplejson as json
import serial
import amiibro

ser = serial.Serial(
    port='/dev/ttyACM0',
    baudrate=9600)
ser.close()
ser.open()


def sendToArduino(command):
    import time
    print("send: %s" % command)
    time.sleep(0.2)
    ser.write(command)
    time.sleep(0.5)
    out=""
    while ser.inWaiting() > 0:
        out += ser.read(1)
    return out

def getStatusFromArduino():
    status = "ffnnn" #sendToArduino("s;")
    ret={'light':(status[0], status[1], status[2]), 'relay': (status[3], status[4])}
    return ret

responses=[]

@route('/')
@route('/<device>/<action>/<channel:int>')
@view('main.tpl')
def main(device=None, action=None, channel=None):
    command="nic"
    if device and action:
        command="%s%s%s;" % (device[0], action[1], channel)
        responses.append(sendToArduino(command))
    status=getStatusFromArduino()
    return dict(status=json.dumps(status),msg = command, responses = responses)

@route('/resetresp')
def resetresponses():
    responses=[]
    return dict()


@route('/amigo/<hex>')
def amiibo(hex=None):
    msgs= amiibro.Amiibro().broforce(hex)
    responses.append(msgs)
    return dict(msg = msgs)


@route('/static/<filename>')
def server_static(filename):
  return static_file(filename, root='./static/')

debug(True)
run(host='0.0.0.0', port=80, reloader=True)
