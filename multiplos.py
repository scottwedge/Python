def multiplos(m, f):
	cont = 0
	cont2 = 0
	for i in range(f):
		cont+=1
		if cont % m == 0:
			cont2+=1
			print cont2
	print "Los multiplos mostrados son ", cont2

multiplos(7, 100)
