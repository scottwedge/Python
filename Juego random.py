def juego_random():
	import random
	n = 0
	cont = 0
	azar = random.randrange(0,100)
	while n != azar:
		n = int(input("Ingrese un numero:"))
		if n > azar:
			print("Menos")
		elif n < azar:
			print("Mas")
		cont += 1
	print ("¡¡¡Acertaste!!!")
	if cont == 1:
		print("Requeriste solo un intento")
	else:
		print("Requeriste",cont,"intentos")

juego_random()
