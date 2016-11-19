def tiempo_viaje():
	n = 1
	total = 0
	while n != 0:
		n = int(input("Ingrese duracion del tramo"))
		total = total + n
	n = total // 60
	total = (n*60) - total
	if total < 0:
		total = total * (-1)
	print (n,":",total)

tiempo_viaje()
