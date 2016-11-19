def cont_vocal():
	a = 0
	e = 0
	i = 0
	o = 0
	u = 0
	n = raw_input("Ingrese una oracion: ")
	for ii in n:
		if ii == 'a':
			a+=1
		elif ii == 'e':
			e+=1
		elif ii == 'i':
			i+=1
		elif ii == 'o':
			o+=1
		elif ii == 'u':
			u+=1
	if a > 0:
		print("Se contaron " + str(a) + " a")
	if e > 0:
		print("Se contaron " + str(e) + " e")
	if i > 0:
		print("Se contaron " + str(i) + " i")
	if o > 0:
		print("Se contaron " + str(o) + " o")
	if u > 0:
		print("Se contaron " + str(u) + " u")
	print("Secuencia Terminada")
