def calculadoraamplia():
	exp = input("Ingresar expresion matematica")
	exp = exp.split(" ")
	for s in range(len(exp)):
		if not exp[s].isalnum():
			a = exp[0:s]
			b = exp[s:len(exp)]
			op = s
	total = a+ b
	return total

calculadoraamplia()
