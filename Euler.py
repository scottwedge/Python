def Euler():
	total = 0
	n3 = 0
	n = -1
	while (1/n3) - (1/n4) >= 0.0001:
		n+=1
		n3 = factorialEuler(n)
		n4 = factorialEuler(n-1)
		total = total + (1/n3)
	return total

Euler()
