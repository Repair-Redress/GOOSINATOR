Bring:
 -	[ ] Goose
 -	[ ] Goose main battery
 -	[ ] Power Pack
 -	[ ] hotspot(s)
 -	[ ] jump charger
 -	[ ] lipo charger
 -	[ ] binocs
 -	[ ] extensions
 -	[ ] multimeter
 -	[ ] camera/s
 -	[ ] Laptop
 -	[ ] SIK for laptop
	

Pre-Check charge on:
 -	[ ] Big Goose
 -	[ ] Video battery
 -	[ ] orbic hotspot
 -	[ ] phone (charge cable)
 -	[ ] laptop (charge)
 -	[ ] jump charger
	
4G tests:
 -	[ ] power autopilot, companion & orbic
 -	[ ] Put mac on phone network, enable wireguard
 -	[ ] test pings / vpn
 -	[ ] test incoming video

SIK test:
 -	[ ] check that radios and talking (bright blinks every second)
 -	[ ] check that primary and secondary comms are showing in QGC

Extra Testing:
 -	[ ] sudo supervisorctl status -> Test supervisord status for temperature stream + mavlink
 -	[ ] Enabling Mavlink in QGC: Enable in Comm Links, set to listen on port 60010
 -	[ ] sudo supervisorctl tail -f temperature -> Checking log of temperature data

Joystick:
 -	[ ] Test that transmitter is showing usb symbol
 -	[ ] Check manual mode -- prop steer and thrust fore/back

PRELAUNCH
 -	[ ] Clean out all missions, logs
 -	[ ] Turn on camera
 -	[ ] Check manual control
 -	[ ] Set auto path in QGC
 -	[ ] Loiter test in addition to manual
