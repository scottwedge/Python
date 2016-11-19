def promprox():
	suma = 0.0
	n = raw_input("Ingrese cada valor separado por un signo '+'(Ej: 9+9+10): ")
	n = n.split('+')
	for i in range(len(n)):
		suma = suma + int(n[i])
	return int(round(suma/len(n)))

promprox()
