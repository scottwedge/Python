def promedio(*notas):
	n = 0
	total = 0
	while n < (len(notas)):
		total = total + notas[n]
		n+=1
	total = total / len(notas)
	print total

promedio(10,9.66,9,9.66,10,9,10,9.33,9.66,9.66,8,9.66,7)
