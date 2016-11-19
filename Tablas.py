def tablas():
	for n in range(1,11):
		for n2 in range(1,11):
			print(n*n2,(" ")*(4-(len(str(n*n2)))),"|",end=" ")
		print()

tablas()
