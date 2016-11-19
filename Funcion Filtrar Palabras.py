def filtrar_palabras(n, string):
	string2 = string.split(" ")
	for stri in string2:
		if len(stri) > n:
			print (stri)

filtrar_palabras(2, "Hola")
