def raiz_multiple(n,r):
	for nn in range(0,n):
		if int(nn**r)==n:
			return nn

raiz_multiple(9,3)
