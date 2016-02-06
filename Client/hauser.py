from bottle import route, run, debug, request, template
import sh

@route('/')
def main_view():
    return template('links_for_actions.tpl', msg= "")
@route('/light/<channel:int>', method='GET')
def light_sender(channel):
    action= request.GET.get('action','').strip()
    command="l%s%s;" % (action, channel)
    message =  "This would be echoed to Arduino Serial Port: %s" % (command)
    return template('links_for_actions.tpl', msg = message)

@route('/relay/<channel:int>', method='GET')
def relay_sender(channel):
    action= request.GET.get('action','').strip()
    command="r%s%s;" % (action, channel)
    message = "This would be echoed to Arduino Serial Port: %s" % (command)
    return template('links_for_actions.tpl', msg = message)

debug(True)

run(port=80, reloader=True)
