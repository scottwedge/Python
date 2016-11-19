def algo_en_comun(p1, p2):
	p1 = p1.lower()
	p2 = p2.lower()
	lista = []
	for i in p1:
		for i2 in p2:
			if i == i2:
				lista.append(i2)
	return lista

algo_en_comun("Hola", "Chau")
