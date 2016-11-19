def CalculadoraSimple():
	exp = input("Ingrese expresion matematica")
	exp2 = exp.split(" ")
	for s in range(len(exp)):
		if not exp[s].isalnum():
			a = int(exp[s-1])
			b = int(exp[s+1])
			if s == '+':
				total = a+b
			elif s == '*':
				total = a*b
			elif s == '-':
				total = a-b
			elif s == '/':
				total = a/b
			else:
				print("Expresion ingresada incorrecta")

CalculadoraSimple()
