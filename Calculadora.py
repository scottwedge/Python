def op(op):
	import math
	if op == '+':
		total = a+b
	elif op == '-':
		total = a-b
	elif op == '*':
		total = a*b
	elif op == '/':
		total = a/b
	elif op == '^':
		total = a**b
	elif op == '|':
		total = math.sqrt(a,b)
	elif op == '%':
		total = a%b
	elif op == '!':
		total = math.factorial(a)
	elif op == '¬':
		total = 1/a
	return total

def exp_multiple():
	exp = input("Ingrese expresion matematica")
	exp = exp.split(" ")
	x1 = exp[0].rstrip(")")
	x1 = x1.lstrip("(")
	x2 = exp[2].rstrip(")")
	x2 = x2.lstrip("(")
	op = exp[1]
	total = op(op)

exp_multiple()
