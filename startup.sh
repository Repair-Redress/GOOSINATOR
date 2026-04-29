#!/bin/bash
# /usr/bin/mavlink-routerd -e 10.2.53.3:60000 -e 10.2.53.4:60001 -e 127.0.0.1:60000 /dev/serial0:115200
/home/pi/.local/bin/mavproxy.py --daemon --master=/dev/serial0 --baudrate 115200 --out 10.2.53.3:60000
/usr/bin/python3 /home/pi/sensor_component.py
