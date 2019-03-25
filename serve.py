import os
import glob
import subprocess
import time
from bottle import route, run, template

def read_temp_raw(fn):
    f = open(fn, 'r')
    lines = f.readlines()
    f.close()
    return lines

def read_temp(f):
    lines = read_temp_raw(f)
    while lines[0].strip()[-3:] != 'YES':
        time.sleep(0.2)
        lines = read_temp_raw(f)
    equals_pos = lines[1].find('t=')
    if equals_pos != -1:
        temp_string = lines[1][equals_pos+2:]
        temp_c = float(temp_string) / 1000.0
        return temp_c

@route('/')
def index():
    return 'Go Away.'

@route('/ac/:switch')
def ac(switch=0):
    if switch == '0':
        rtn = subprocess.call(["irsend", "SEND_ONCE", "mitsubishi", "OFF"])
        # rtn should equal 0 if command ran without error
        return '<h1 style="text-align: center; padding-top: 40%; font-size: 100px;">switching off</h1>'

    elif switch == '1':
        rtn = subprocess.call(["irsend", "SEND_ONCE", "mitsubishi", "ON"])
        # rtn should equal 0 if command ran without error
        time.sleep(2)
        rtn = subprocess.call(["irsend", "SEND_ONCE", "mitsubishi", "FAN"])
        # rtn should equal 0 if command ran without error
        return '<h1 style="text-align: center; padding-top: 40%; font-size: 100px;">switching on</h1>'

    elif int(switch) > 1:
        p = subprocess.Popen(['/home/pi/pistat/timer.py', switch]);
        return '<h1 style="text-align: center; padding-top: 40%; font-size: 85px;">switching on for ' + switch + ' minutes</h1>'

@route('/temp')
def temp():
    os.system('modprobe w1-gpio')
    os.system('modprobe w1-therm')

    base_dir = '/sys/bus/w1/devices/'
    device_folder = glob.glob(base_dir + '28*')[0]
    device_file = device_folder + '/w1_slave'

    return '<h1 style="text-align: center; padding-top: 40%; font-size: 100px;">temp is ' + str(read_temp(device_file)) + '</h1>'

run(host='0.0.0.0', port=8765, server="meinheld")