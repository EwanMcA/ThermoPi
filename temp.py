import os
import glob
import time

# Set up thermometer kernel modules and readout location
def setup():
    os.system('modprobe w1-gpio')
    os.system('modprobe w1-therm')

    base_dir = '/sys/bus/w1/devices/'
    device_folder = glob.glob(base_dir + '28*')[0]
    device_file = device_folder + '/w1_slave'
    return device_file

# Read raw data from disk
def read_temp_raw(fn):
    f = open(fn, 'r')
    lines = f.readlines()
    f.close()
    return lines

# Read data and return parsed temperature
def read_temp(f):
	# Read raw temperature data (including boilerplate junk)
    lines = read_temp_raw(f)
	
	# Loop until temp is available
    while lines[0].strip()[-3:] != 'YES':
        time.sleep(0.2)
        lines = read_temp_raw(f)

    # Strip out junk and return temperature
	equals_pos = lines[1].find('t=')
	if equals_pos != -1:
        temp_string = lines[1][equals_pos+2:]
        temp_c = float(temp_string) / 1000.0
        return temp_c

# Print current temp at 1 second intervals
def debug_temp():
    while True:
        print("    " + str(read_temp()))
        time.sleep(1)