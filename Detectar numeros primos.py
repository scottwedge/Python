def n_primos(nn):
	for n in range(1,nn):
		for n2 in range(1,10):
			if n % n2 == 0 and n != n2 and n2 != 1:
				break
		else:
			print (n)

n_primos(100)
