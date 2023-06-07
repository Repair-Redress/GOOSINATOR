# Notes on setup
We tried using dronekit to save temp file separately as a log file. Then tried looking at Mavrouter. Finally settled for a combination of pymavlink and mavproxy to broadcast the mavlink signal and inject it with a mavlink general purpose field.

## MavProxy
Setting up mavproxy for echoing between goose, laptop, qgroundcontrol.
Using pymavink/mavutil to inject h20 temp into mavlink log

This sends link to mac qgroundcontrol but also local loopback:
mavproxy.py --master=/dev/serial0 --baudrate 115200 --out 10.2.53.3:60000 --out 127.0.0.1:14550

On goose I had to give permission to serial: 
sudo usermod -a -G tty pi

Another process  can tap in here:
mavproxy.py --master=udp:127.0.0.1:60000

## PyMavlink
Some interesting examples:
https://www.ardusub.com/developers/pymavlink.html#send-message-to-qgroundcontrol

For process sending temperature, I was able to find info on a random way of sending values:
https://discuss.bluerobotics.com/t/adding-a-sensor-to-mavlink-stream/7985/22
using the function master.mav.named_value_float_send()

pseudoexample
```
from pymavlink import mavutil
# Create the connection to the top-side computer as companion computer/autopilot
master = mavutil.mavlink_connection('udpout:10.2.53.3:14550', source_system=1)
master.mav.named_value_float_send(
    int((time.time() - boot_time) * 1e3), # Unix time since boot (milliseconds)
    sensor_name,
    temp
    )
```

## Post Processing
Example of dumping qgroundcontrol tlog to text:
mavlogdump.py --planner --format standard Documents/QGroundControl\ Daily/Telemetry/2023-05-18\ 17-35-20.tlog > temp2.txt

