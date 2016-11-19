def LCD(n3):
	for n in range(1,6):
		for n2 in range(n3):
			if n % 2 != 0:
				print("-",end=" ")
			else:
				print("|",end=" ")
		print()

LCD(16)
