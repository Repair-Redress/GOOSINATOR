# Take the sensor and report it to ground control
# TODO change hardcoded sensor names, IP addresses in the VPN, etc. to rely on env 
# variables or a config

from tsys01_python import tsys01
import datetime
import os
import shutil

################################################################################
#
# Temperature sensor
#
################################################################################
sensor = tsys01.TSYS01()

if not sensor.init():
    print("Error initializing sensor")
    exit(1)

################################################################################
#
# PyMavlink
#
################################################################################

import time
boot_time = time.time()
sensor_name = b'H2O_TEMP'

# Import mavutil
from pymavlink import mavutil
# Create the connection to the top-side computer as companion computer/autopilot
master = mavutil.mavlink_connection('udpout:10.2.53.3:14550', source_system=1)

################################################################################
#
# Put It All Together
#
################################################################################

while(1):
    # temperature sensor, might fail
    try:
        sensor.read()
        temp = sensor.temperature()
        tempstring = f"{temp:.3f}"
        print(temp)
    except:
        print("error reading sensor!")
        temp = -273.16

    master.mav.named_value_float_send(
        int((time.time() - boot_time) * 1e3), # Unix time since boot (milliseconds)
        sensor_name,
        temp
        )
    time.sleep(1)
