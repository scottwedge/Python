def histo2():
	n = 1
	pos = 0
	neg = 0
	print ("Ingrese varios valores, termine con 0")
	while n != 0:
		n = int(input())
		if n >= 0:
			pos+=1
		else:
			neg+=1
	print ("Positivos = ",'*'*pos)
	print ("Negativos = ",'*'*neg)

histo2()
