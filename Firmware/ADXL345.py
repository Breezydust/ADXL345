#Library Imports
import time
import board
import busio
import adafruit_adxl34x

#Sensor initialization
i2c = busio.I2C(board.SCL, board.SDA)
sensor = adafruit_adxl34x.ADXL345(i2c)


mode = input("Simple or Advanced Measurements? ")


if mode.lower() == "advanced": #enable more sensor functionality
	print("Enabling advanced measurements")
	sensor.enable_freefall_detection(threshold=10, time=25) #enable freefall detection with a threshold of 625mg of force (10*62.5mg) and a time scale of less than 125ms (25x5)
	sensor.enable_motion_detection(threshold=18) #enable motion detection with a threshold of 1125mg (18x62.5mg) of force
	sensor.enable_tap_detection(tap_count=1, threshold=20, duration=50, latency=20, window=0) #enable tap detection. detects single taps, tap intensity threshold is 1250mg, minimum duration is 50ms, latency to register single tap is 20ms
else:
	print("Using only simple measurements")

while True:
	print("X: %f Y: %f Z: %f"%sensor.acceleration) #print X, Y and Z coordinates and any acceleration
	if bool(sensor.events["freefall"]): print("Sensor dropped!")	#advanced funtionality - print sensor dropped if freefall is detected
	if bool(sensor.events["tap"]): print("Sensor tapped!")		#advanced functionality - print sensor tapped if tap is detected
	if bool(sensor.events["motion"]): print("Sensor moved!")	#advanced functionality - print sensor moved if movement is detected
	time.sleep(1.0)
