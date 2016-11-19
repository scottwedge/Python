def sumparimpar():
	cont = 0
	suma = 0
	suma2 = 0
	for i in range(100):
		cont+=1
		if cont % 2 == 0:
			suma+=cont
		else:
			suma2+=cont
	print "Suma de pares: ", suma
	print "Suma de impares ", suma2

sumparimpar()
