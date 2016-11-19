def buscarenlista():
	n = int(input("Digame la cantidad de palabras:"))
	lista = []
	for nn in range(1,n+1):
		print ("Digame la palabra",nn,":",end=" ")
		n2 = input()
		lista += [n2]
	s = input("Digame la palabra a buscar:")
	n = lista.count(s)
	print ("La palabra",s,"aparece",n,"veces")

buscarenlista()
