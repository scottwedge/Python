def invertir_lista():
	n = int(input("Digame la cantidad de palabras:"))
	lista = []
	for nn in range(1,n+1):
		print ("Digame la palabra",nn,":",end=" ")
		n2 = input()
		lista += [n2]
	lista2 = []
	for i in range(len(lista)-1,-1,-1):
		lista2 += [lista[i]]
	print(lista2)

invertir_lista()
