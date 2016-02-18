from bottle import route, run, debug, template, view, static_file
import serial

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
    status = sendToArduino("s;")
    ret={'light':(status[0],status[1],status[2]), 'relay':(status[3],status[4])}
    return status


responses=[]
@route('/')
@route('/<device>/<action>/<channel:int>')
@view('main.tpl')
def main(device=None, action=None, channel=None):
    command="nic"
    if device and action:
        command="%s%s%s;" % (device[0], action[1], channel)
        responses.append(sendToArduino(command))
    import simplejson as json
    status=getStatusFromArduino()
    return dict(status=json.dumps(status),msg = command, responses = responses)

@route('/amigo/<hex>')
def broforce(hex=None):
    responses.append(hex)
    return dict(msg=hex)

@route('/static/<filename>')
def server_static(filename):
  return static_file(filename, root='./static/')


debug(True)
run(host='0.0.0.0', port=80, reloader=True)
