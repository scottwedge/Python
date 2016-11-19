def sustituirenlista():
	n = int(input("Digame la cantidad de palabras:"))
	lista = []
	for nn in range(1,n+1):
		print ("Digame la palabra",nn,":",end=" ")
		n2 = input()
		lista += [n2]
	b = input("Ingrese la palabra a sustituir:")
	s = input("por la palabra:")
	for i in range(len(lista)):
                if lista[i] == b:
                        lista[i] = s
        print (lista)

sustituirenlista()
