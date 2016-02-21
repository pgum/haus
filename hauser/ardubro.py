import simplejson as json
import serial

class Ardubro:
    def __init__(self, port='/dev/ttyACM0', baud=9600):
        self.ser = serial.Serial(
        port=port,
        baudrate=baud)
        self.ser.close()
        self.ser.open()

    def sendCommand(self, command):
        import time
        print("send: %s" % command)
        time.sleep(0.2)
        self.ser.write(command)
        time.sleep(0.3)
        out=""
        while self.ser.inWaiting() > 0:
            out += ser.read(1)
        return out

    def getStatus(self):
        status = "ffnnnn" #sendCommand("s;")
        ret={'light': (status[0], status[1], status[2]), 'relay': (status[4], status[5])}
        return ret


