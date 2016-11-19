def mult(lista):
	n1 = len(lista)
	n = 0
	n2 = 0
	total = 1
	while n < n1:
		n2 = lista[n]
		total = total * n2
		n+=1
	return total

mult(1,2,3,4)
