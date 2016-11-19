from os import system

def printer():
	cont = 0;
	while True:
		system("cls")
		cont+=1
		if cont == 4:
			cont = 0
		if cont == 0:
			print "|"
		elif cont == 1:
			print "/"
		elif cont == 2:
			print "-"
		elif cont == 3:
			print "\ "

printer()