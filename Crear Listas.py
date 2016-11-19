def crear_lista():
	n = int(input("Digame la cantidad de palabras:"))
	lista = []
	for nn in range(1,n+1):
		print ("Digame la palabra",nn,":",end=" ")
		n2 = input()
		lista += [n2]
	print ("La lista creada es:",lista)

crear_lista()
