def multiplos(m, f):
    cont, lista = 0, 0, []
    for i in range(f):
        cont+=1
	if cont % m != 0:
            lista.append(cont)
    return lista

no_multiplos(3, 100)
