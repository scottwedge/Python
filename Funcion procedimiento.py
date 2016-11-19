def procedimiento(n1, n2, n3):
	st = 0
	nn = 0
	n = 0
	while st < 3:
		st+=1
		if st == 1:
			n = n1
		elif st == 2:
			n = n2
		elif st == 3:
			n = n3
		s = ""
		nn = 0
		while nn < n:
			nn+=1
			s = s + "*"
		print (s)

procedimiento(1, 2, 3)
