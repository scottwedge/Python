def codigo():
	tupla = (" ", "n", "g", "t", "d", "w", "c", "o", "x", "q", "j", "m", "s", "v", "e", "k", "b", "f", "z", "p", "h", "a", "r", "y", "u", "l", "i")
	subcodigo = ""
	n = 0
	n2 = 1
	total = ""
	codigo = input("Ingrese el codigo\n")
	codigo = codigo.replace(" ", "0")
	tipo = codigo.isalpha()
	if tipo == 1:
                codigo = codigo.replace("0", " ")
        else:
                print ("Error: Caracteres no alfanumericos ingresados")
                codigo()
	subcodigo = codigo[:1]
	tipo = subcodigo.isalpha()
	if tipo == 1 :
		while n2 != (len(codigo)+1):
                        subcodigo = codigo[:n2]
                        while subcodigo != tupla[n]:
                                if subcodigo != tupla[n]:
                                        n+=1
                                else:
                                        total = total + str(n)
                                        n2+=1
	else:
                n3 = len(codigo)
		while n2 != (n3 + 1):
                        subcodigo = codigo[:n2]
                        while subcodigo != tupla[n]:
                                if subcodigo != tupla[n]:
                                        n+=1
                                else:
                                        total = total + str(n)

codigo()
