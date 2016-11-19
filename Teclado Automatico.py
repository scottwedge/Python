def teclado():
	for n in range(1,6):
		for n2 in range(6):
			if n == 2:
				print("|",n2,end=" ")
			elif n == 4:
				print("|",n2+4,end=" ")
			else:
				print("-"*3,end=" ")
		print()

teclado()
