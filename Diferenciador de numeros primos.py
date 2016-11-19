def diferenciador(n):
	n2 = 1
	while n2 < 10:
		if n % 2 == 0 and n != n2 and n2 != 1:
			return "Es compuesto"
		else:
			n2+=1
	return "Es primo"

diferenciador(4)
