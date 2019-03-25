import sys
import time

import ac

if len(sys.argv) != 2:
    print('usage: timer <minutes>')
else:
    ac.send(ac.ACCommand.ON)
    time.sleep(2)
    ac.send(ac.ACCommand.FAN)

    time.sleep(60 * int(sys.argv[1]))

    ac.send(ac.ACCommand.OFF)