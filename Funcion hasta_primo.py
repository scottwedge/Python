def hasta_primo(nn):
	cont = 0
	n = 1
	while cont < nn+1:
		for n2 in range(1,10):
			if n % n2 == 0 and n != n2 and n2 != 1:
				n+=1
				break
		else:
			print (n)
			cont+=1
			n+=1

hasta_primo(100)
