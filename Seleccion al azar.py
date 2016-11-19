def azar():
        import random
	co ,c1 = 1, 1
	while co == c1:
		azar = bin(random.randrange(1000))
		c1 = str(azar).count("1")
		c0 = str(azar).count("0")
	if c1 > c0:
		return True
	else:
		return False

azar()
