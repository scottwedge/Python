import re

def red():
	try:
		string = "Hoy quiero trabajar"
		if re.search(r'trabaj('')', string):
			print "Correcto"
	except Exception as e:
		print e
	raw_input()

red()