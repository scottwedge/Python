def tabla():
	n = int(input("Ingrese un numero\n"))
	n2 = 1
	while n2 <= 10:
		total = n * n2
		print (n," x ",n2," = ",total)
		n2+=1

tabla()
