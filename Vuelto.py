def vuelto():
	costo = input("Ingrese costo:")
	paga = input("Ingrese paga:")
	vuelto = paga - costo
	bil = 100
	while vuelto > 0:
		cont = 0
		while vuelto - bil >= 0:
			vuelto-=bil
			cont+=1
		if cont > 0:
			print str(cont)+" de $"+str(bil)
		if bil > 10:
			bil = int(bil/20)*10
		else:
			bil = int(bil/2)

vuelto()
