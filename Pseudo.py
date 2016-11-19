def Escribir (string="\n"):
    print (string)

def Mostrar (string="\n"):
    print (string)

def Leer (cant_var):
	lista = []
	for i in range(1, cant_var+1):
		lista.append(i)
	for i in range(len(lista)):
		lista[i]=raw_input()
	return lista

def Contador(n, mostrar=0):
	n+=1
	if mostrar==1:
		print n
	return n

def ParaN(inicio=0, fin, paso=1, funcion, n=0):
	for i in range(inicio, fin, paso):
		n = funcion(n)

def Si(var1, exp, var2):
	if exp == '=' or exp == '==':
		if var1 == var2:
			return True
		else:
			return False
	elif exp == '<':
		if var1 < var2:
			return True
		else:
			return False
	elif exp == '>':
		if var1 > var2:
			return True
		else:
			return False
	elif exp == '>=' or exp == '=>':
		if var1 >= var2:
			return True
		else:
			return False
	elif exp == '<=' or exp == '=<':
		if var1 <= var2:
			return True
		else:
			return False
	elif exp == '!=' or exp == '=!':
		if var1 != var2:
			return True
		else:
			return False
	else:
		raise "SyntaxError"

def Retorno(booleana, fTrue, fFalse):
	if booleana == True:
		fTrue()
	else:
		fFalse()


