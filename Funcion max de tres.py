def max_de_tres(n1,n2,n3):
	if n1 > n2 and n1 > n3:
		return n1
	elif n2 > n1 and n2 > n3:
		return n2
	elif n3 > n1 and n3 > n2:
		return n3
	else:
		return "Los tres numeros son iguales"

max_de_tres(1,2,3)