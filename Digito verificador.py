def dig_ver():
	n = int(input("Ingrese digito a verificar:"))
	n2 = str(n)[::-1]
	n4 = 2
	total = 0
	for n3 in range(len(n2)):
		total = total + (int(n2[n3]) * n4)
		n4+=1
		if n4 == 8:
			n4 = 2
	total = total % 11
	total = 11 - total
	total = n - total
	return total

dig_ver()
