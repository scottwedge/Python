def answer(x):
	pot, cont = 1, 0
	ult = ""
	lista = []
	while pot < x:
		pot *= 3
		cont += pot
		if ult == "L":
			lista.append("-")
		else:
			lista.append("L")
			ult = "L"
	lista.append("R")
	return lista

print answer(8)