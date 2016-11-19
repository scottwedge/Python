def cant_mayus(string):
	leng = len(string)
	s = ""
	total = 0
	n = 0
	while n < leng:
		n+=1
		s = string[:n]
		s = s.isupper()
		if s == 1:
			total+=1
	return total

cant_mayus("Hola")
