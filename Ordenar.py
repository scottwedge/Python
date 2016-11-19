def orden():
	lista = [1, 4, 3, 9, 2, 4]
	lista2 = []
	for i in range(len(lista)):
		if lista2 == []:
			lista2.append(lista[i])
		else:
			for i2 in range(len(lista2)):
				if i2 == range(len(lista2)):
					lista2.insert(-1, lista[i])
					break
				if lista[i] > lista2[i2] or lista[i] == lista2[i2]:
					lista2.insert(0, lista[i])
					break
	return lista2
