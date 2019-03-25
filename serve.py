import glob
import subprocess
import time
from bottle import route, run, template

import ac
import temp

# Syntactic sugar for simple HTML response
def msg_tmpl(message, fntSize):
        return '''<h1 style="text-align: center; padding-top: 40%; font-size: {0}px;">
                                {1}
                          </h1>'''.format(fntSize, message)

# Don't want the root to return anything at the moment
@route('/')
def index():
    return 'Go Away.'

# The route is used to delineate AC commands
@route('/ac/:switch')
def ac_toggle(switch=0):

        # Switch it off
    if switch == '0':
        ac.send(ac.ACCommand.OFF)
        return msg_tmpl("switching off", 100)

        # Switch it on and set to max fan
    elif switch == '1':
        ac.send(ac.ACCommand.ON)
        time.sleep(2)
        ac.send(ac.ACCommand.FAN)
        return msg_tmpl("switching on", 100)

        # Switch it on for x minutes
    elif int(switch) > 1:
        p = subprocess.Popen(['/home/pi/pistat/timer.py', switch]);
        return msg_tmpl("switching on for " + switch + " minutes", 85)

@route('/temp')
def temp_display():
        # Return the current temperature
    return msg_tmpl('temp is ' + '{:.1f}'.format(temp.read_temp(temp.setup())) + ' C', 100)

run(host='0.0.0.0', port=8765, server="meinheld")