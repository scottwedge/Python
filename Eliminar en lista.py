def eliminarenlista():
	n = int(input("Digame la cantidad de palabras:"))
	lista = []
	for nn in range(1,n+1):
		print ("Digame la palabra",nn,":",end=" ")
		n2 = input()
		lista += [n2]
	s = input("Ingrese la palabra que desea eliminar:")
	for i in range(len(lista)):
		if lista[i] == s:
			lista.pop(i)
	print (lista)

eliminarenlista()
