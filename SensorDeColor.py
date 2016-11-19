def SensorDeColor():
	import serial
	import numpy as np
	import cv2
	from time import sleep
	Arduino = serial.Serial('COM4', 9600, timeout = 1)
	for i in range(0,3,1):
		valores[i]=Arduino.readline()
		sleep(1000)
	img = np.zeros((300,512,3), np.uint8)
	cv2.namedWindow('Sensor de Color', cv2.WINDOW_NORMAL)
	cv2.imshow('Colores',img)
	while(1):
		k=cv2.waitKey(1) & 0xFF
		if k==27:
			break
		img[:]=[b,g,r]
	cv2.destroyAllWindows()

SensorDeColor()
