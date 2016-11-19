def suma_primos():
	nn = int(input("Ingrese numero a factorear"))
	for n in range(1,nn):
		for n2 in range(1,10):
			if n % n2 == 0 and n != n2 and n != 0:
				break
		else:
			total = nn - n
			for n2 in range(1,10):
				if total % n2 == 0 and total != n2 and n2 != 0:
					break
			else:
                                print (n,"+",total,"=",n)

suma_primos()
