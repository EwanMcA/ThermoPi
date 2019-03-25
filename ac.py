import os
import subprocess
from enum import Enum

# Simple enum for instructions which have been recorded
class ACCommand(Enum):
	OFF = 1
	ON = 2
	FAN = 3
	
# Send an instruction with irsend (using labels which are stored in LIRC config)
def ac_command(command=ACCommand.OFF):
	
	if command == ACCommand.OFF:
		label = "OFF"
	elif command == ACCommand.ON:
		label = "ON"
	elif command == ACCommand.FAN:
		label = "FAN"
	
	# Use irsend to blast the correct sequence to the AC
	return subprocess.call(["irsend", "SEND_ONCE", "mitsubishi", label])