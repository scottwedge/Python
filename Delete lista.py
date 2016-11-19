def Dellista():
	n = int(input("Ingrese la cantidad de palabras:"))
	lista = []
	for nn in range(1,n+1):
		print ("Ingrese la palabra",nn,":",end=" ")
		n2 = input()
		lista += [n2]
	n2 = int(input("Ingrese la cantidad de palabras:"))
	lista2 = []
	for nn in range(1,n+1):
		print ("Ingrese la palabra",nn,":",end=" ")
		n2 = input()
		lista2 += [n2]
	for i in range(len(lista2)):
		for j in range(len(lista)):
			if lista2[i] == lista[j]:
				del(lista[j])
	print(lista)

Dellista()
