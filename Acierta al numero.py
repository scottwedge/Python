def acierto_game():
	from random import randrange
	try:
		while True:
			rango = input("Introduzca un numero: ")
			azar = randrange(rango)
			user = 0
			while user < 1 or user > 100:
				user = input("Ingrese un numero del 1 al " + str(rango) + ": ")
			if azar == user:
				"Felicitaciones, acerto al numero"
			else:
				print "No acerto al numero"
				print "El numero era", azar
				print "Intentelo nuevamente\n"
	except:
		print "Saliendo..."

acierto_game()
