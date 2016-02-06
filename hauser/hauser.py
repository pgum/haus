from bottle import route, run, debug, request, template
import sh

def sendToArduino(command):                                                                                                
    sh.echo(command, _out="/dev/ttyACM0");                                                                                 

@route('/')                                                                                                                
def main_view():                                                                                                           
    return template('links_for_actions.tpl', msg= "")                                                                      
@route('/<device>/<channel:int>', method='GET')                                                                               
def device_sender(device, channel):                                                                                                 
    action= request.GET.get('action','').strip()                                                                           
    command="%s%s%s;" % (device[0], action, channel)                                                                                   
    sendToArduino(command)                                                                                                 
    return template('links_for_actions.tpl', msg = command)                                                                
                                                                                                                           
debug(True)
run(host='0.0.0.0', port=80, reloader=True)
