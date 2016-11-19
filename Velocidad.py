def velocidad():
	distancia = input("Introduzca la distancia: ")
	tiempo = input("Introduzca el tiempo requerido: ")
	velocidad = (distancia*1000) / (tiempo*60)
	print "Velocidad en m/s: ", velocidad


velocidad()
