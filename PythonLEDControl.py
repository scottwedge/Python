def PythonLEDControl():
	import serial
	Arduino = serial.Serial('COM4', 9600, timeout=1)
	while(1):
		n=input("Introduzca un '1' para prender el LED o un '0' para apagar")
		if n==1:
			Arduino.write(chr(1))
		else:
			Arduino.write(chr(0))

PythonLEDControl()
