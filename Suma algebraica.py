def suma_algebraica():
	lista = [-2,5,8,-9,10,15,-4]
	i,x,pos,neg = 0,0,0,0
	for i in range(0,len(lista),1):
		x = lista[i]
		if x >= 0:
			pos=pos+x
		else:
			neg=neg+x
	print "La suma de positivos es: ", pos
	print "La suma de negativos es: ",neg

suma_algebraica()
